import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ---------------- LOAD DATA ----------------
data = pd.read_csv("train.csv")

# clean column names
data.columns = data.columns.str.strip()

# ---------------- HANDLE MISSING ----------------
data['Gender'] = data['Gender'].fillna(data['Gender'].mode()[0])
data['Married'] = data['Married'].fillna(data['Married'].mode()[0])
data['Self_Employed'] = data['Self_Employed'].fillna(data['Self_Employed'].mode()[0])
data['Dependents'] = data['Dependents'].fillna(data['Dependents'].mode()[0])

data['LoanAmount'] = data['LoanAmount'].fillna(data['LoanAmount'].median())
data['Loan_Amount_Term'] = data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mode()[0])
data['Credit_History'] = data['Credit_History'].fillna(data['Credit_History'].mode()[0])


# ---------------- FIX DEPENDENTS ----------------
data['Dependents'] = data['Dependents'].replace('3+', 3)
data['Dependents'] = data['Dependents'].astype(int)

# ---------------- ENCODING ----------------
data['Gender'] = data['Gender'].map({'Male':1,'Female':0})
data['Married'] = data['Married'].map({'Yes':1,'No':0})
data['Education'] = data['Education'].map({'Graduate':1,'Not Graduate':0})
data['Self_Employed'] = data['Self_Employed'].map({'Yes':1,'No':0})
data['Property_Area'] = data['Property_Area'].map({'Urban':2,'Semiurban':1,'Rural':0})
data['Loan_Status'] = data['Loan_Status'].map({'Y':1,'N':0})

# ---------------- FEATURES ----------------
X = data.drop(['Loan_ID','Loan_Status'], axis=1)
y = data['Loan_Status']

# ---------------- SPLIT ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ---------------- MODEL ----------------
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=7,
    random_state=42
)

model.fit(X_train, y_train)

# ---------------- EVALUATION ----------------
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

# ---------------- SAVE ----------------
pickle.dump(model, open("loan_model.pkl","wb"))
print("Model saved as loan_model.pkl")
