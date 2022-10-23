from typing import Union

from fastapi import FastAPI

from models.user import UserModel

import pickle

from ml_models.ml_model import predict_defaulter

from models.prediction import Prediction

app = FastAPI()

@app.get("/")
def read_root():
    return "CREDIT RISK MANAGEMENT API"


@app.post("/predict", response_model=UserModel)
def predict(user: UserModel):
    with open('./model_files/model.bin', 'rb') as f_in:
        model = pickle.load(f_in)
        f_in.close()
    predictions = predict_defaulter(user, model)
    return Prediction(defaulter_prediction=[list(predictions)])