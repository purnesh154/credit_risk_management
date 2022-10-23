from typing import Union

from fastapi import FastAPI

from models.user import UserModel

import pickle

from models.ml_model import predict_defaulter

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
    result = {
        'defaulter_prediction': list(predictions)
    }
    return result