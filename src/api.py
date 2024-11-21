from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Crear la instancia de FastAPI
app = FastAPI()

# Cargar el modelo previamente entrenado
model = joblib.load("notebooks\best_model.joblib")

# Clase para entrada de datos
class Transaction(BaseModel):
    amount: float
    category: str
    age: int
    gender: str

# Endpoint de predicción
@app.post("/predict/")
def predict(transaction: Transaction):
    # Convertir datos a DataFrame
    data = pd.DataFrame([transaction.dict()])
    prediction = model.predict(data)
    return {"fraud_prediction": bool(prediction[0])}
