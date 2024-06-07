from typing import Union
from fastapi import FastAPI, HTTPException
import joblib
import numpy as np

app = FastAPI()

# Initialize the Service

# Uncomment and load your model file as needed
# model_file = "./model/XXX.joblib"
# model = joblib.load(model_file)

admin_password = ""

# Default Section ==============================================================

@app.get("/")
def read_root():
    # Return Report or status
    return {"Hello": "World"}

# Training Model Section ==============================================================

@app.post("/add_sample", tags=["Training Section"])
def add_sample(var1: float, var2: float, var3: float, var4: float):
    # Add samples to the training dataset
    return {"message": f"add {var1} {var2} {var3} {var4}"}

@app.post("/train", tags=["Training Section"])
def train():
    # Populate data and re fitting
    # Get performance metric (RMSE etc.)
    return {"message": f"Model trained successfully with RMSE: {4.332}"}

@app.post("/commit", tags=["Training Section"])
def commit():
    # Populate - Re-train Model - Save to file
    # Retrieve Model
    return {"message": f"Model has been updated"}

# Prediction Section ==============================================================

@app.get("/predict", tags=["Prediction Section"])
def predict(
    soil_type: str,
    temp: float,
    humid: float,
    ph: float,
    n: float,
    p: float,
    k: float,
    ec: float
):
    # Add model prediction logic here
    # For demonstration, let's assume we have a model for each soil type
    # And we predict the values using the loaded model
    if soil_type not in ['clay', 'sand', 'silt']:
        raise HTTPException(status_code=400, detail="Invalid soil type")

    # Load the appropriate model based on soil type
    # model = joblib.load(f"./model/{soil_type}_model.joblib")
    # For the purpose of this example, let's assume a dummy prediction
    features = np.array([[temp, humid, ph, n, p, k, ec]])
    # prediction = model.predict(features)
    
    # Dummy prediction
    prediction = {"lab_pH": 7.0, "lab_N": 10.0, "lab_P": 20.0, "lab_K": 30.0, "lab_EC": 1.0}

    return prediction
