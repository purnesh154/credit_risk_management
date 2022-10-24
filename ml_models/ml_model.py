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

def predict_defaulter(user,model):
    config = {
    'person_age': user.person_age,
    'person_income':user.person_income,
    'person_home_ownership':user.person_home_ownership,
    'person_emp_length':user.person_emp_length,
    'loan_intent':user.loan_intent,
    'loan_grade':user.loan_grade,
    'loan_amnt':user.loan_amnt,
    'loan_int_rate':user.loan_int_rate,
    'loan_percent_income':user.loan_percent_income,
    'cb_person_default_on_file':user.cb_person_default_on_file,
    'cb_person_cred_hist_length':user.cb_person_cred_hist_length
    }
    if type(config) == dict:
        data = pd.DataFrame(config)
    else:
        data = config
    data = preprocess(data)
    data = normalize(data)
    y_pred = model.predict(data)
    for i in range (0,y_pred.size):
        if y_pred[i]>0.5:
            y_pred[i]=1
        else:
            y_pred[i]=0
    return y_pred.astype(int)