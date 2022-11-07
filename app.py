from typing import Union
from fastapi import FastAPI, APIRouter, Request, Form
from models.prediction import Prediction
from models.user import UserModel
import pickle
from ml_models.ml_model import predict_defaulter
from models.prediction import Prediction
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()
@app.get("/")
def read_root():
    return "CREDIT RISK MANAGEMENT API"

@app.get("/predict")
def form_post(request: Request):
    person_age = "Enter Person's Age",
    person_income="Enter Person's Income",
    person_home_ownership = "Enter Home Ownership Status",
    person_emp_length = "Enter Employment Length",
    loan_intent = "Enter Loan Intent",
    loan_grade = "Enter Loan_Grade",
    loan_amnt = "Enter Loan Amount",
    loan_int_rate = "Enter Interest Rate",
    loan_percent_income = "Enter Loan Percent Income",
    cb_person_default_on_file = "Enter Historical default",
    cb_person_cred_hist_length = "Enter Credit history length"
    return templates.TemplateResponse('./static/form.html',context={'request': request, 'person_age': person_age, 'person_income': person_income, 'person_home_ownership': person_home_ownership, 'person_emp_length': person_emp_length, 'loan_intent': loan_intent, 'loan_grade': loan_grade, 'loan_amnt': loan_amnt, 'loan_int_rate': loan_int_rate, 'loan_percent_income': loan_percent_income, 'cb_person_default_on_file': cb_person_default_on_file, 'cb_person_cred_hist_length': cb_person_cred_hist_length})



@app.post("/predict", response_model=Prediction)
def predict(user: UserModel):
    with open('./ml_models/model.bin', 'rb') as f_in:
        model = pickle.load(f_in)
        f_in.close()
    predictions = predict_defaulter(user, model)
    return Prediction(defaulter_prediction=[predictions])
def form_post(request: Request, person_age: int = Form(...), person_income: int = Form(...), person_home_ownership: str = Form(...), person_emp_length: int = Form(...), loan_intent: str = Form(...), loan_grade: str = Form(...), loan_amnt: int = Form(...), loan_int_rate: float = Form(...), loan_percent_income: float = Form(...), cb_person_default_on_file: str = Form(...), cb_person_cred_hist_length: int = Form(...)):
    user: UserModel
    user.person_age = person_age
    user.person_income = person_income
    user.person_home_ownership = person_home_ownership
    user.person_emp_length = person_emp_length
    user.loan_intent = loan_intent
    user.loan_grade = loan_grade
    user.loan_amnt = loan_amnt
    user.loan_int_rate = loan_int_rate
    user.loan_percent_income = loan_percent_income
    user.cb_person_default_on_file = cb_person_default_on_file
    user.cb_person_cred_hist_length = cb_person_cred_hist_length
    defaulter : Prediction 
    defaulter = predict(user)
    return templates.TemplateResponse('./static/form.html', context={'request': request, 'defaulter': defaulter})