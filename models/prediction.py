from pydantic import BaseModel

class Prediction(BaseModel):
    defaulter_prediction: list[str]