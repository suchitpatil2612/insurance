import streamlit as st
from preprocessing import acc
import pandas as pd

def app():
    st.subheader("Select values: ")

    age = st.slider("Age",0,100)
    sex = st.radio("Gender",["Male", "Female"])
    bmi = st.slider("BMI",0.0,35.0)
    children = st.slider("Number of Childs",0,10)
    smoker = st.radio("Smoker",["Yes","No"])
    region = st.selectbox("Region", ["northwest", "northeast", "southeast", "southwest"])

    if (region == "northwest"):
        region = 0
    elif (region == "northeast"):
        region = 1
    elif (region == "southeast"):
        region = 2
    else:
        region = 3

    if (sex == "Male"):
        sex = 0
    else:
        sex = 1

    if (smoker == "No"):
        smoker = 0
    else:
        smoker = 1


    feature = [[age, sex, bmi, children, smoker, region]]

    if (st.button("PREDICT")):
        mymodel, accuracy = acc()
        prediction = mymodel.predict(feature)

        st.success("Predicted Successfully")
        st.success(f"Our Model Accuracy is: {round(accuracy,2)}")
        st.info(f"Charges value: {round(prediction[0],2)}")

