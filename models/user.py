from pydantic import BaseModel
"""{
  "person_age": [
    22
  ],
  "person_income": [
    20000
  ],
  "person_home_ownership": [
    "OWN"
  ],
  "person_emp_length": [
    5.0
  ],
  "loan_intent": [
    "VENTURE"
  ],
  "loan_grade": [
    "C"
  ],
  "loan_amnt": [
    10000
  ],
  "loan_int_rate": [
    8.84
  ],
  "loan_percent_income": [
    0.55
  ],
  "cb_person_default_on_file": [
    "N"
  ],
  "cb_person_cred_hist_length": [
    4
  ]
}
python -m uvicorn app:app --reload"""
class UserModel(BaseModel):
    person_age: list[int]
    person_income: list[int]
    person_home_ownership: list
    person_emp_length: list[float]
    loan_intent: list
    loan_grade: list
    loan_amnt : list[int]
    loan_int_rate: list[float]
    loan_percent_income: list[float]
    cb_person_default_on_file: list
    cb_person_cred_hist_length: list[int]