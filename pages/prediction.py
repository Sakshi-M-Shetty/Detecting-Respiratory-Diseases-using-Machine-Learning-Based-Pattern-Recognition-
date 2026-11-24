import streamlit as st
import numpy as np
import joblib

st.title(" Disease Prediction")

model = joblib.load("respiratory_model.pkl")
scaler = joblib.load("scaler.pkl")

col1,col2 = st.columns(2)

with col1:

    fvc = st.number_input("FVC",1.0,8.0,4.0)

    fev1 = st.number_input("FEV1",0.5,6.0,3.0)

    ratio = st.number_input("FEV1/FVC",40.0,100.0,80.0)

    pef = st.number_input("PEF",1.0,15.0,7.0)

with col2:

    fef25 = st.number_input("FEF25",0.5,10.0,5.0)

    fef50 = st.number_input("FEF50",0.5,10.0,4.5)

    fef75 = st.number_input("FEF75",0.5,10.0,4.0)

    fef2575 = st.number_input("FEF25_75",0.5,10.0,4.2)

if st.button("Predict Disease"):

    sample = np.array([[
        fvc,
        fev1,
        ratio,
        pef,
        fef25,
        fef50,
        fef75,
        fef2575
    ]])

    sample = scaler.transform(sample)

    prediction = model.predict(sample)[0]

    confidence = np.max(
        model.predict_proba(sample)
    )*100

    st.success(
        f"Predicted Disease : {prediction}"
    )

    st.progress(int(confidence))

    st.info(
        f"Confidence Score : {confidence:.2f}%"
    )