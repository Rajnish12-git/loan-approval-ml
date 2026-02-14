# 🏦 Loan Approval Prediction System

An end-to-end Machine Learning web application that predicts whether a loan application will be approved or rejected based on applicant financial details.

The project integrates a trained ML model with a FastAPI backend and a React frontend for real-time predictions.

---

## 🚀 Features

* Predict loan approval instantly
* Real banking dataset (Kaggle Loan Prediction)
* REST API using FastAPI
* Interactive React user interface
* ~87% model accuracy
* Full stack ML deployment ready

---

## 🧠 Machine Learning

* Algorithm: Random Forest Classifier
* Dataset: Loan Prediction Dataset (Dream Housing Finance)
* Preprocessing:

  * Missing value handling
  * Categorical encoding
  * Feature engineering
* Evaluation: Train/Test Split Accuracy

---

## 🏗 Tech Stack

**Frontend**

* React.js
* CSS

**Backend**

* FastAPI
* Uvicorn

**Machine Learning**

* Python
* Pandas
* Scikit-learn
* NumPy

---

## 📂 Project Structure

```
LoanApprovalSystem
│
├── backend
│   ├── predict_api.py
│   ├── loan_model.pkl
│   ├── requirements.txt
│
└── loan-frontend
```

---

## ▶ Run Locally

### Backend

```
cd backend
python -m uvicorn predict_api:app --reload
```

### Frontend

```
cd loan-frontend
npm install
npm run dev
```

---

## 📊 Sample Prediction

Input:

* Income: 5000
* Credit History: Good
* Property Area: Urban

Output:

```
Loan Approved ✅
```

---

## 👨‍💻 Author

Rajnish Kumar
