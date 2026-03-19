from fastapi import FastAPI, HTTPException
import pandas as pd
import pickle
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Load the pre-trained model
try:
    model = pickle.load(open("movie_dict.pkl", 'rb'))
except FileNotFoundError:
    raise RuntimeError("Model file not found. Please ensure 'movie_dict.pkl' exists.")

# # Define the input data model using Pydantic
# class CarInput(BaseModel):
#     company: str
#     year: int
#     kms_driven: int
#     fuel_type: str

# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}

# # Define the prediction endpoint
# @app.post("/predict")
# def predict_price(car: CarInput):
#     try:
#         # Create input data for prediction
#         input_data = pd.DataFrame([[car.company, car.year, car.kms_driven, car.fuel_type]], 
#                                   columns=['company', 'year', 'kms_driven', 'fuel_type'])
        
#         print("Input Data:", input_data)  # Debugging: Print input data
        
#         # Ensure the input data has the same structure as the training data
#         expected_columns = ['company', 'year', 'kms_driven', 'fuel_type']  # Replace with actual columns used during training
#         if set(input_data.columns) != set(expected_columns):
#             raise HTTPException(status_code=400, detail="Input data columns do not match training data columns.")
        
#         # Make prediction
#         prediction = model.predict(input_data)
#         print("Prediction:", prediction)  # Debugging: Print prediction
        
#         return {"predicted_price": float(prediction[0])}
#     except Exception as e:
#         print("Error:", str(e))  # Debugging: Print the error
#         raise HTTPException(status_code=500, detail=str(e))