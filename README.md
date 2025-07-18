
# EV2 - Modelos de Regresión

Esta rama corresponde a la **segunda etapa del proyecto**, centrada en la implementación y evaluación de **modelos de regresión** para estimar el rendimiento ofensivo de un jugador durante una partida de CS:GO.

---

## 🎯 Objetivo

Desarrollar modelos de regresión capaces de **predecir la cantidad de kills (MatchKills)** que un jugador puede obtener, a partir de diversas estadísticas de combate recolectadas durante una partida.

---

## 📊 Variables utilizadas

Se utilizaron como predictores variables relevantes del rendimiento del jugador:

- `headshots`
- `time_alive`
- `distance_travelled`



---

## 🧠 Modelos evaluados

Se compararon diferentes algoritmos de regresión, entre ellos:

- **Regresión Lineal Simple**
- **Regresión Lineal Múltiple**
- **Árbol de Decisión (Decision Tree)**
- **Random Forest Regressor**
- **Soporte Vectorial Machine**

---

## 📈 Métricas de evaluación

Los modelos fueron evaluados usando las siguientes métricas:

- **MAE** (Error Absoluto Medio)
- **RMSE** (Raíz del Error Cuadrático Medio)
- **R²** (Coeficiente de Determinación)

Estas métricas permiten medir el error promedio y la capacidad explicativa del modelo.

---

## 🔄 Continuación del proyecto

La siguiente etapa del proyecto, en la rama `EV3`, se enfocó en la **clasificación**: predecir si una partida será ganada o perdida según variables similares.

---
