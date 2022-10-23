from pydantic import BaseModel

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