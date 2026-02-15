import { useState } from "react";
import "./App.css";

export default function App() {

  const [result, setResult] = useState("");

  const [form, setForm] = useState({
    Gender: 1,
    Married: 1,
    Dependents: 0,
    Education: 1,
    Self_Employed: 0,
    ApplicantIncome: 5000,
    CoapplicantIncome: 0,
    LoanAmount: 120,
    Loan_Amount_Term: 360,
    Credit_History: 1,
    Property_Area: 2
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: Number(e.target.value) });
  };

  const predict = async () => {
    const query = new URLSearchParams(form).toString();
    const res = await fetch(`https://loan-approval-ml-yiq9.onrender.com/predict?${query}`, {
  method: "POST"
});
    
    const data = await res.json();
    setResult(data.prediction);
  };

  return (
    <div className="page">
      <div className="card">
        <h2>Loan Approval Predictor</h2>

      <div className="field">
  <label>Gender</label>
  <select name="Gender" onChange={handleChange}>
    <option value="1">Male</option>
    <option value="0">Female</option>
  </select>
</div>

<div className="field">
  <label>Married</label>
  <select name="Married" onChange={handleChange}>
    <option value="1">Yes</option>
    <option value="0">No</option>
  </select>
</div>

<div className="field">
  <label>Dependents</label>
  <input type="number" name="Dependents" onChange={handleChange}/>
</div>

<div className="field">
  <label>Education</label>
  <select name="Education" onChange={handleChange}>
    <option value="1">Graduate</option>
    <option value="0">Not Graduate</option>
  </select>
</div>

<div className="field">
  <label>Self Employed</label>
  <select name="Self_Employed" onChange={handleChange}>
    <option value="0">No</option>
    <option value="1">Yes</option>
  </select>
</div>

<div className="field">
  <label>Applicant Income</label>
  <input type="number" name="ApplicantIncome" onChange={handleChange}/>
</div>

<div className="field">
  <label>Coapplicant Income</label>
  <input type="number" name="CoapplicantIncome" onChange={handleChange}/>
</div>

<div className="field">
  <label>Loan Amount</label>
  <input type="number" name="LoanAmount" onChange={handleChange}/>
</div>

<div className="field">
  <label>Loan Term (months)</label>
  <input type="number" name="Loan_Amount_Term" onChange={handleChange}/>
</div>

<div className="field">
  <label>Credit History</label>
  <select name="Credit_History" onChange={handleChange}>
    <option value="1">Good</option>
    <option value="0">Bad</option>
  </select>
</div>

<div className="field">
  <label>Property Area</label>
  <select name="Property_Area" onChange={handleChange}>
    <option value="2">Urban</option>
    <option value="1">Semiurban</option>
    <option value="0">Rural</option>
  </select>
</div>


        <button onClick={predict}>Check Eligibility</button>

        {result && (
          <p className={result.includes("Approved") ? "approved" : "rejected"}>
            {result}
          </p>
        )}
      </div>
    </div>
  );
}
