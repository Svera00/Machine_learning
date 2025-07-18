# app/main.py
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import joblib
import numpy as np
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

features_info = {
    'TeamStartingEquipmentValue': (0, 36150, "¿Valor total del equipamiento inicial de tu equipo?"),
    'RoundStartingEquipmentValue': (0, 8850, "¿Valor del equipamiento con el que iniciaste esta ronda?"),
    'MatchKills': (0, 41, "¿Cuántos kills hiciste en la partida completa?"),
    'MatchHeadshots': (0, 22, "¿Cuántos headshots hiciste en la partida completa?"),
    'MatchAssists': (0, 14, "¿Cuántas asistencias hiciste en la partida completa?"),
}

CLASS_FEATURES = list(features_info.keys())

base_models_path = os.path.join("app", "models")
clf_model_path = os.path.join(base_models_path, "csgo_pipeline.pkl")
reg_model_path = os.path.join(base_models_path, "csgo_regression_rf.pkl")

clf_model = joblib.load(clf_model_path)
reg_model = joblib.load(reg_model_path)

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "input_data": {},
            "selected_model": "classification",
            "features_info": features_info,
            "prediction": None
        },
    )

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request):
    form = await request.form()
    model_type = form.get("model_type", "classification")
    prediction = None

    # Convertir formulario en diccionario y manejar vacíos
    input_data = dict(form)

    if model_type == "classification":
        # Validación segura
        input_values = {}
        for f in CLASS_FEATURES:
            val = form.get(f, "")
            try:
                input_values[f] = float(val) if val else 0.0
            except ValueError:
                input_values[f] = 0.0

        input_array = np.array([[input_values[f] for f in CLASS_FEATURES]])
        prediction_raw = clf_model.predict(input_array)[0]
        prediction = "GANASTE" if prediction_raw == 1 else "NO GANASTE"

    else:
        mh_raw = form.get("MatchHeadshots_reg", "")
        try:
            mh = float(mh_raw) if mh_raw else 0.0
        except ValueError:
            mh = 0.0
        input_array = np.array([[mh]])
        pred_value = reg_model.predict(input_array)[0]
        prediction = f"MatchKills estimados: {pred_value:.2f}"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "input_data": input_data,
            "prediction": prediction,
            "selected_model": model_type,
            "features_info": features_info,
        },
    )
