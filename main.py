import streamlit as st
import pages
import pandas as pd


st.title("Insurance Prediction App")
st.write("This uses Linear Regression")


st.sidebar.title("Navigation")
page = st.sidebar.radio("Pages", ["Home", "Pages"])

if (page == "Pages"):
    pages.app()