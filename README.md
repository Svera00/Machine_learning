# Machine_learning


Este repositorio contiene el desarrollo de un proyecto de Machine Learning aplicado a partidas del videojuego **CS:GO**. Se exploraron distintos enfoques de regresión y clasificación con el objetivo de analizar el rendimiento de los jugadores y predecir resultados.

---

## 📂 Estructura del repositorio

El proyecto está organizado en **cuatro ramas**:

### 🔹 `EV1` - Análisis Exploratorio (EDA)
- Se realizó análisis exploratorio de los datos.
- Se identificaron patrones iniciales y relaciones entre variables como `headshots`, `Matchkills`, `time_alive`, entre otras.
- Visualización de distribuciones y correlaciones.

### 🔹 `EV2` - Modelos de Regresión
- Se implementaron modelos de regresión para estimar el número de **kills (matchkills)** a partir de variables como:
  - `headshots`
  - `time_alive`
  - `distance_travelled`, entre otras.
- Se evaluó el rendimiento con métricas como **MAE**, **RMSE**, **R²**
- Modelos evaluados: Random Forest, Decission Tree, Regresión Lineal,Regresion Multiple, SVM.

### 🔹 `EV3` - Modelos de Clasificación
- Se construyeron modelos para predecir si un jugador **ganará o perderá** una partida.
- Variables utilizadas:
  - `headshots`, `Matchassists`, etc.
- Modelos evaluados: Random Forest, Decission Tree, Regresión Logística, SVM, KNN.
- Métricas: **accuracy**, **precision**, **recall**, **f1-score**.

### 🔹 `ET` - Entrega Final
- Contiene la estructura final del proyecto.
- Incluye todo el código limpio, organizado y listo para revisión o presentación.
- **Los modelos `.pkl` no están en el repositorio debido a restricciones de tamaño**. Puedes descargarlos desde los siguientes enlaces:

---

## 📦 Modelos entrenados

Los modelos finales entrenados se encuentran disponibles en Google Drive:

🔸 **Modelo de Regresión (`csgo_regression_rf.pkl`)**  
📥 [Descargar desde Drive](https://drive.google.com/file/d/1gNh1gsIWe4UZMTfhQ3bU0wbXJZ1pc4Gj/view?usp=sharing)

🔸 **Modelo de Clasificación (`csgo_classifier.pkl`)**  
📥 [Descargar desde Drive](https://drive.google.com/file/d/1BVjpOrPrXqWn07ZrlefgH5Ht8zmm0Bpa/view?usp=sharing)

> Para ejecutar el código que los utiliza, asegúrate de colocar los modelos en la ruta `app/models/`.

---

## ✅ Requisitos
- fastapi
- uvicorn
- scikit-learn
- imblearn
- pandas
- numpy
- jinja2
- joblib
- Python 3.x
- Scikit-learn
- Pandas
- NumPy
- Matplotlib / Seaborn (opcional para visualización)

Puedes instalar los requerimientos con:

```bash
pip install -r requirements.txt
