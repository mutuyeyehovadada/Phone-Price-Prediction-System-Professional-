# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 21:55:05 2025
@author: Chantal.Uwase
"""

import streamlit as st
import numpy as np
#import joblib
import pickle

# Load the saved model
with open('save.pkl','rb') as file:
    model=pickle.load(file)

def main():
    # --- App Title ---
    st.title("📱 Phone Price Prediction App")

    # --- Load the Trained Model ---
   #-- model_path = "C:/Users/Chantal.Uwase/Desktop/ML_14OCT/phone_price.pkl"
    #---model = joblib.load(model_path)

    st.markdown("### Enter Phone Specifications")

    # --- User Inputs ---
    resoloution = st.number_input("Screen Resolution (inches)", 4.0, 8.0, 5.5)
    ram = st.number_input("RAM (GB)", 1, 12, 4)
    battery = st.number_input("Battery Capacity (mAh)", 1000, 6000, 3000)
    thickness = st.number_input("Thickness (mm)", 5.0, 12.0, 9.5)

    # --- Prediction Button ---
    if st.button("🔮 Predict Price"):
        # Prepare features (make sure order matches your training data)
        features = np.array([[resoloution, ram, battery, thickness]])

        # Predict
        prediction = model.predict(features)

        # Show result
        st.success(f"💰 Predicted Phone Price: {prediction[0]:,.2f}$")

if __name__ == '__main__':
    main()
