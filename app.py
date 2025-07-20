

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import datetime

# Load the trained model
# Make sure 'car_price_prediction' file is in the same directory or provide the full path
try:
    car_price_prediction = joblib.load('car_price_prediction')
except FileNotFoundError:
    st.error("Model file 'car_price_prediction' not found. Please ensure the model file is in the correct location.")
    st.stop()

st.title('Car Price Prediction App')

st.write("""
Enter the details of the car to get a predicted selling price.
""")

# Create input widgets
present_price = st.slider('Present Price (in Lakhs)', min_value=0.0, max_value=35.0, value=7.0, step=0.1)
kms_driven = st.slider('Kms Driven', min_value=0, max_value=100000, value=50000, step=1000)
fuel_type = st.selectbox('Fuel Type', options=['Petrol', 'Diesel', 'CNG'])
seller_type = st.selectbox('Seller Type', options=['Dealer', 'Individual'])
transmission = st.selectbox('Transmission', options=['Manual', 'Automatic'])
owner = st.slider('Number of Owners', min_value=0, max_value=3, value=1, step=1)
year = st.slider('Year of Purchase', min_value=1990, max_value=datetime.datetime.now().year, value=2015, step=1)

# Map categorical inputs to numerical values used in training
fuel_type_mapping = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
seller_type_mapping = {'Dealer': 0, 'Individual': 1}
transmission_mapping = {'Manual': 0, 'Automatic': 1}

fuel_type_encoded = fuel_type_mapping[fuel_type]
seller_type_encoded = seller_type_mapping[seller_type]
transmission_encoded = transmission_mapping[transmission]

# Calculate the age of the car
dt = datetime.datetime.now()
old = dt.year - year

# Create a DataFrame from the input
new_data = pd.DataFrame({
    'Present_Price': [present_price],
    'Kms_Driven': [kms_driven],
    'Fuel_Type': [fuel_type_encoded],
    'Seller_Type': [seller_type_encoded],
    'Transmission': [transmission_encoded],
    'Owner': [owner],
    'Old': [old]
})

# Predict the price
if st.button('Predict Price'):
    try:
        predicted_price = car_price_prediction.predict(new_data)[0]
        st.success(f"Predicted Selling Price: ₹ {predicted_price:.2f} Lakhs")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

