from pydantic import BaseModel


"""
'person_age': [24, 26, 28],
    'person_income':[10000, 40000, 60000],
    'person_home_ownership':['OWN', 'RENT', 'MORTGAGE'],
    'person_emp_length':[2, 4, 6],
    'loan_intent':['MEDICAL', 'EDUCATION', 'DEBTCONSOLIDATION'],
    'loan_grade':['D', 'B' ,'A'],
    'loan_amnt':[50000, 80000, 100000],
    'loan_int_rate':[8.14, 9.26, 10.18],
    'loan_percent_income':[0.55, 0.57, 0.59],
    'cb_person_default_on_file':['N', 'N', 'Y'],
    'cb_person_cred_hist_length':[2, 2, 4]
"""

class UserModel(BaseModel):
    person_age: list[int]
    person_income: list[int]
    person_home_ownership: list[str]
    person_emp_length: list[float]
    loan_intent: list[str]
    loan_grade: list[str]
    loan_amnt : list[int]
    loan_int_rate: list[float]
    loan_percent_income: list[float]
    cb_person_default_on_file: list[str]
    cb_person_cred_hist_length: list[int]
