# EV3 - Modelos de Clasificación

Esta rama corresponde a la **tercera etapa del proyecto**, enfocada en el desarrollo y evaluación de **modelos de clasificación** para predecir el resultado de una partida de CS:GO (victoria o derrota) a partir de distintas variables de rendimiento del jugador.

---

## 🎯 Objetivo

Construir modelos de Machine Learning capaces de **predecir si un jugador ganará o perderá una partida**, basándose en variables recolectadas durante cada ronda o partida.

---

## 📊 Variables utilizadas

Las siguientes variables fueron seleccionadas para el entrenamiento de los modelos:

- `headshots`
- `MatchAssists`
- `RoundFlankKills`
- `TravelledDistance`
- `TimeAlive`
- `RoundWinner`

---

## 🧠 Modelos evaluados

Se entrenaron y compararon los siguientes modelos de clasificación:

- **Random Forest**
- **Árbol de Decisión (Decision Tree)**
- **Regresión Logística**
- **Máquinas de Vectores de Soporte (SVM)**
- **K-Nearest Neighbors (KNN)**

---

## 📈 Métricas de evaluación

Para evaluar el rendimiento de los modelos, se utilizaron las siguientes métricas:

- **Accuracy** (Exactitud)
- **Precision**
- **Recall** (Sensibilidad)
- **F1-Score**
- **Matriz de Confusión**

Estas métricas permiten tener una visión completa del desempeño de los modelos, especialmente en problemas con clases desbalanceadas.

---

## 🧪 Resultados

Los mejores resultados fueron obtenidos con el modelo **Support vector machine**, que mostró buen equilibrio entre precisión y recall.


---

## 📌 Nota adicional

La rama `EV3` contiene el código específico para clasificación. Para la entrega final, con todo el código o
