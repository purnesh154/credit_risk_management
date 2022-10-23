import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from models.user import UserModel

def preprocess(data):
    data["person_home_ownership"] = data["person_home_ownership"].map({'OWN':0, 'MORTGAGE':1, 'RENT':2, 'OTHER':3})
    data["loan_intent"] = data["loan_intent"].map({'EDUCATION':0, 'MEDICAL':1, 'VENTURE':2, 'PERSONAL':3, 'HOMEIMPROVEMENT':4, 'DEBTCONSOLIDATION':5})
    data["loan_grade"] = data["loan_grade"].map({'B':0, 'C':1, 'A':2, 'D':3, 'E':4, 'F':5, 'G':6})
    data["cb_person_default_on_file"] = data["cb_person_default_on_file"].map({'N':0, 'Y':1})
    return data

def normalize(data):
    sc = StandardScaler()
    data = sc.fit_transform(data)
    return data

def predict_defaulter(config,model):
    if type(config) == UserModel:
        data = pd.DataFrame(config)
    else:
        data = config
    data = preprocess(data)
    data = normalize(data)
    y_pred = model.predict(data)
    return y_pred.astype(int)