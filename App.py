import streamlit as st
import pandas as pd
import joblib

model = joblib.load("car_price_model.pkl")

st.title("Car Price Predictor")

present_price = st.number_input("Present Price (in Lakhs)", min_value=0.0, step=0.1)
kms_driven = st.number_input("Kilometers Driven", min_value=0)
owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])
car_age = st.slider("Car Age (in years)", min_value=0, max_value=30, value=5)

fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel'])
seller_type = st.selectbox("Seller Type", ['Dealer', 'Individual'])
transmission = st.selectbox("Transmission", ['Manual', 'Automatic'])

fuel_type_petrol = 1 if fuel_type == 'Petrol' else 0
fuel_type_diesel = 1 if fuel_type == 'Diesel' else 0
seller_type_individual = 1 if seller_type == 'Individual' else 0
transmission_manual = 1 if transmission == 'Manual' else 0


input_df = pd.DataFrame([{
    'Present_Price': present_price,
    'Kms_Driven': kms_driven,
    'Owner': owner,
    'Car_age': car_age,
    'Fuel_Type_Diesel': fuel_type_diesel,
    'Fuel_Type_Petrol': fuel_type_petrol,
    'Seller_Type_Individual': seller_type_individual,
    'Transmission_Manual': transmission_manual
}])

if st.button("Predict Resale Price"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Resale Price: ₹{round(float(prediction[0]), 2)} Lakh")