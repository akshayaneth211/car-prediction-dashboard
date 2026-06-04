import streamlit as st
import numpy as np
import pickle
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))

st.title("🚗 Car Price Prediction App")

year = st.number_input("Year", 2010, 2025, 2020)
mileage = st.number_input("Mileage", 0, 200000, 20000)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel"])

fuel_diesel = 1 if fuel == "Diesel" else 0

input_data = np.array([[year, mileage, fuel_diesel]])

if st.button("Predict Price"):
    price = model.predict(input_data)
    st.success(f"Predicted Price: ₹ {price[0]:,.0f}")
