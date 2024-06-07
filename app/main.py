from typing import Union

from fastapi import FastAPI
import joblib

app = FastAPI()

# Initialize the Service

#model_file = "./model/XXX.joblib"
#model = joblib.load(model_file)

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
    
    # Get performace metric (RMSE etc.)
    
    return {"message": f"Model trained successfully with RMSE: {4.332}"}

@app.post("/commit", tags=["Training Section"])
def commit():
    
    # Populate - Re-train Model - Save to file
    
    # Retreive Model
    
    return {"message": f"Model has been updated"}


# Prediction Section ==============================================================

@app.get("/predict", tags=["Prediction Section"])
def predict(var1: float, var2: float, var3: float, var4: float):
    
    return {"message": f"add {var1} {var2} {var3} {var4}"}