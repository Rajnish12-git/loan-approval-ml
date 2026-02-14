from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import pickle
import pandas as pd

# load trained model
model = pickle.load(open("loan_model.pkl", "rb"))

app = FastAPI(title="Loan Approval Prediction API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Loan Prediction API Running"}

@app.post("/predict")
def predict(
    Gender:int,
    Married:int,
    Dependents:int,
    Education:int,
    Self_Employed:int,
    ApplicantIncome:float,
    CoapplicantIncome:float,
    LoanAmount:float,
    Loan_Amount_Term:float,
    Credit_History:float,
    Property_Area:int
):
    
    # create dataframe in same order as training
    data = pd.DataFrame([[
        Gender, Married, Dependents, Education, Self_Employed,
        ApplicantIncome, CoapplicantIncome, LoanAmount,
        Loan_Amount_Term, Credit_History, Property_Area
    ]],
    columns=[
        'Gender','Married','Dependents','Education','Self_Employed',
        'ApplicantIncome','CoapplicantIncome','LoanAmount',
        'Loan_Amount_Term','Credit_History','Property_Area'
    ])

    prediction = model.predict(data)[0]

    if prediction == 1:
        result = "Loan Approved ✅"
    else:
        result = "Loan Rejected ❌"

    return {"prediction": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)

