import streamlit as st
import joblib
import numpy as np
import pandas as pd

# 1. LOAD MODEL AND SCALER
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

st.set_page_config(page_title="Credit Wise Loan System", layout="wide")
st.title("🏦 Credit Wise: Advanced Loan Approval System")

# 2. USER INPUTS (Organized for better UI)
st.header("Applicant Information")
col1, col2, col3 = st.columns(3)

with col1:
    applicant_income = st.number_input("Applicant Monthly Income", value=5000)
    coapplicant_income = st.number_input("Coapplicant Monthly Income", value=0)
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, value=0)

with col2:
    savings = st.number_input("Current Savings Balance", value=2000)
    existing_loans = st.number_input("Number of Existing Loans", value=0)
    credit_score = st.slider("Credit Score", 300, 850, 650)
    education = st.selectbox("Education Level (0=Undergrad, 1=Grad)", [0, 1])

with col3:
    loan_amount = st.number_input("Requested Loan Amount", value=15000)
    loan_term = st.number_input("Loan Term (Months)", value=36)
    collateral = st.number_input("Collateral Value", value=0)

st.header("Additional Details")
c1, c2, c3, c4 = st.columns(4)

with c1:
    employment = st.selectbox("Employment Status", ["Salaried", "Self-employed", "Unemployed"])
with c2:
    marital = st.selectbox("Marital Status", ["Married", "Single"])
with c3:
    purpose = st.selectbox("Loan Purpose", ["Car", "Education", "Home", "Personal", "Other"])
with c4:
    property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

gender = st.radio("Gender", ["Female", "Male"], horizontal=True)
employer = st.selectbox("Employer Category", ["Government", "MNC", "Private", "Unemployed", "Other"])

# 3. PREDICTION LOGIC
if st.button("Analyze Loan Eligibility"):
    # Initialize 27 features with 0
    data = [0.0] * 27
    
    # Map Numerical Values (Positions 0-9)
    data[0] = applicant_income
    data[1] = coapplicant_income
    data[2] = age
    data[3] = dependents
    data[4] = existing_loans
    data[5] = savings
    data[6] = collateral_value = collateral
    data[7] = loan_amount
    data[8] = loan_term
    data[9] = education 

    # Map One-Hot Encoded Categories (Positions 10-24)
    if employment == "Salaried": data[10] = 1
    if employment == "Self-employed": data[11] = 1
    if employment == "Unemployed": data[12] = 1
    
    if marital == "Single": data[13] = 1
    
    if purpose == "Car": data[14] = 1
    if purpose == "Education": data[15] = 1
    if purpose == "Home": data[16] = 1
    if purpose == "Personal": data[17] = 1
    
    if property_area == "Semiurban": data[18] = 1
    if property_area == "Urban": data[19] = 1
    
    if gender == "Male": data[20] = 1
    
    if employer == "Government": data[21] = 1
    if employer == "MNC": data[22] = 1
    if employer == "Private": data[23] = 1
    if employer == "Unemployed": data[24] = 1

    # Final Calculated/Squared Features (Positions 25-26)
    # Ensure these calculations match what you did in Jupyter
    dti = (loan_amount / (applicant_income + 1)) 
    data[25] = dti**2 # DTI_Ratio_Sq
    data[26] = credit_score**2 # Credit_Score_sq

    # 4. SCALE AND PREDICT
    # Conver to 2D array and scale
    input_array = np.array([data])
    scaled_data = scaler.transform(input_array)
    
    prediction = model.predict(scaled_data)
    
    st.divider()
    if prediction[0] == 1:
        st.success("🎉 LOAN APPROVED: Low risk profile detected.")
    else:
        st.error("⚠️ LOAN REJECTED: High risk of default based on provided data.")