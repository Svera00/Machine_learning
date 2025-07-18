import os
import pandas as pd
from sklearn.utils import resample
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
import joblib

# Construir ruta absoluta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "ET_demo_round_traces_2022.csv")

df = pd.read_csv(DATA_PATH, sep=';', low_memory=False, dtype=str)

# === 2. Variables
features = [
    'MatchKills', 'MatchAssists', 'MatchHeadshots',
    'RoundKills', 'RoundAssists', 'RoundHeadshots',
    'RoundFlankKills', 'TravelledDistance', 'TimeAlive',
    'RoundStartingEquipmentValue', 'TeamStartingEquipmentValue'
]
target = 'MatchWinner'

# === 3. Limpieza
df_clean = df[features + [target]].dropna().copy()
df_clean[target] = df_clean[target].astype(int)

for col in features:
    df_clean[col] = (
        df_clean[col]
        .astype(str)
        .str.replace('.', '', regex=False)
        .str.replace(',', '.', regex=False)
        .astype(float)
    )

X = df_clean[features]
y = df_clean[target]

# === 4. Balanceo
ros = RandomOverSampler(random_state=42)
X_bal, y_bal = ros.fit_resample(X, y)

# === 5. Split + escalado
X_train, X_test, y_train, y_test = train_test_split(X_bal, y_bal, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# === 6. Entrenar SVM RBF
svm_rbf = SVC(kernel='rbf', probability=True, random_state=42)
svm_rbf.fit(X_train_scaled, y_train)

# === 7. Guardar modelo y scaler
joblib.dump(svm_rbf, "checkpoints/svm_model.pkl")
joblib.dump(scaler, "checkpoints/scaler.pkl")

print(f"Modelo entrenado. Accuracy en test: {svm_rbf.score(X_test_scaled, y_test):.2f}")
