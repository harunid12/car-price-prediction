from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

# Load model
model = joblib.load("model/ridge.pkl")

app = FastAPI(
    title="Car Price Prediction API",
    description="Predict car selling price using Ridge Regression model",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Request Body
class CarInput(BaseModel):
    Present_Price: float
    Kms_Driven: int
    Past_Owners: int
    Age: int
    Fuel_Type_Diesel: bool
    Fuel_Type_Petrol: bool
    Seller_Type_Individual: bool
    Transmission_Manual: bool

@app.post("/predict")
def predict_price(data: CarInput):

    # Convert boolean → int (model expect 0/1)
    input_data = np.array([[
        data.Present_Price,
        data.Kms_Driven,
        data.Past_Owners,
        data.Age,
        int(data.Fuel_Type_Diesel),
        int(data.Fuel_Type_Petrol),
        int(data.Seller_Type_Individual),
        int(data.Transmission_Manual)
    ]])

    # Predict price dalam satuan Lacs (Lakhs)
    pred_lacs = float(model.predict(input_data)[0])

    # Konversi Lacs → Rupee
    rupee = pred_lacs * 100000

    # Konversi Rupee → Rupiah
    kurs = 190  
    rupiah = rupee * kurs

    return {
        "predicted_price_lacs": round(pred_lacs, 2),
        "predicted_price_rupiah": int(rupiah)
    }

