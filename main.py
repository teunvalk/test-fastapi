# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 11:57:14 2023

@author: teun_
"""

from fastapi import FastAPI

# import uvicorn
import pickle

app = FastAPI(debug=True)

@app.get('/')
def home():
    return {"text": "Car Pricing Prediction Solution"}

@app.get('/predict')
def  predict(Year: str, Kms_Driven: str, Owner: str,
Fuel_Type_Diesel: str, Fuel_Type_Petrol: str, Seller_Type_Individual: str, Transmission_Manual: str):
    
    model = pickle.load(open("C:/Users/teun_/OneDrive - Valuso AI/Valuso AI - General/00 Development/FastAPI/random_forest_model.pkl","rb"))
    makeprediction = model.predict([[Year, Kms_Driven, Owner, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]])
    output = round(makeprediction[0],2)

    return {f"You can sell your car for {output}"}

# if __name__ == "__main__":
#     uvicorn.run(app)