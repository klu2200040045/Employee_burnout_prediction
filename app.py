import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the saved model and scaler using pickle
with open('employee_burnout_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Function to preprocess, scale, and predict burnout rate
def predict_burn_rate(gender, company_type, wfh_setup, designation, resource_allocation, mental_fatigue_score):
    # Validate inputs
    if not gender or not company_type or not wfh_setup:
        st.error("All fields must be filled before submission!")
        return None

    # One-hot encode the gender column
    gender_male = 1 if gender == 'Male' else 0

    # Create a DataFrame with user inputs
    input_data = pd.DataFrame({
        'Designation': [designation],
        'Resource Allocation': [resource_allocation],
        'Mental Fatigue Score': [mental_fatigue_score],
        'Company Type_Service': [1 if company_type == 'Service' else 0],
        'WFH Setup Available_Yes': [1 if wfh_setup == 'Yes' else 0],
        'Gender_Male': [gender_male]
    })

    # Scale the input data
    input_data_scaled = scaler.transform(input_data)

    # Make the prediction
    prediction = model.predict(input_data_scaled)
    return prediction[0]

# Streamlit web app UI
st.title('Employee Burnout Prediction')

# Create input fields for the user
gender = st.selectbox('Gender', ['', 'Male', 'Female'])  # Default to empty for validation
company_type = st.selectbox('Company Type', ['', 'Service', 'Product'])
wfh_setup = st.selectbox('WFH Setup Available', ['', 'Yes', 'No'])
designation = st.number_input('Designation', min_value=1, max_value=5, step=1, value=1)
resource_allocation = st.number_input('Resource Allocation', min_value=0.0, max_value=10.0, step=0.1, value=0.0)
mental_fatigue_score = st.number_input('Mental Fatigue Score', min_value=0.0, max_value=10.0, step=0.1, value=0.0)

# When the user clicks on 'Predict', make the prediction
if st.button('Predict Burnout Rate'):
    if not gender or not company_type or not wfh_setup:
        st.error("Please ensure all dropdowns are selected!")
    else:
        burn_rate = predict_burn_rate(
            gender=gender,
            company_type=company_type,
            wfh_setup=wfh_setup,
            designation=designation,
            resource_allocation=resource_allocation,
            mental_fatigue_score=mental_fatigue_score
        )
        if burn_rate is not None:
            st.success(f'Predicted Burnout Rate: {burn_rate:.2f}')
