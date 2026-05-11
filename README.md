# 🏦 Credit Wise: Advanced Loan Approval System

[![Streamlit App](http://192.168.31.102:8501)

## 📌 Project Overview
Credit Wise is an end-to-end Machine Learning application designed to automate the loan underwriting process. By analyzing 27 key financial and demographic variables, the system provides a real-time risk assessment to determine whether a loan applicant is likely to be approved or rejected.

This project demonstrates the transition of a model from a research environment (Jupyter Notebook) to a production-ready web application.

## 🚀 Live Demo
**Check out the live app here:** [Link to your Streamlit App](http://192.168.31.102:8501)

## 🛠️ Tech Stack
*   **Language:** Python
*   **Machine Learning:** Scikit-Learn (Naive Bayes Classifier)
*   **Deployment:** Streamlit Cloud
*   **Data Handling:** Pandas, NumPy
*   **Model Persistence:** Joblib

## 📊 Features & Data
The model evaluates applicants based on **27 features**, including:
*   **Financial Metrics:** Applicant Income, Coapplicant Income, Loan Amount, Savings, and DTI Ratio.
*   **Demographics:** Age, Marital Status, Education Level, and Gender.
*   **Risk Factors:** Credit Score (Squared), Existing Loans, and Employment Status.

The application includes a robust **preprocessing pipeline** that handles one-hot encoding for categorical variables and applies **StandardScaling** to ensure high prediction accuracy.

## 📁 Project Structure
```text
├── app.py                # Main Streamlit application code
├── model.pkl             # Trained Naive Bayes model
├── scaler.pkl            # StandardScaler object for data normalization
├── requirements.txt      # List of dependencies for deployment
├── README.md             # Project documentation
└── Credit_Wise.ipynb     # Original development and training notebook