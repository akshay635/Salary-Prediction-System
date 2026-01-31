# -*- coding: utf-8 -*-
# app.py

#importing the required libraries
import streamlit as st
from src.prediction import predict
from src.exploration import explore
import importlib
import src.config as config

importlib.reload(config)

# set page configuration
# Subtitle: Predict your earnings with clean data and powerful machine learning models

st.set_page_config(page_title=config.APP_TITLE, 
                   page_icon=config.APP_ICON, 
                   layout=config.PAGE_LAYOUT)

# title
st.markdown("""
    <div style='text-align: center;'>
        <h1>Smart Salary Estimator</h1>
        <h4 style='color: gray;'>Predict your earnings with clean data and powerful ML models</h4>
    </div>
""", unsafe_allow_html=True)

# page dropdown
page = st.sidebar.selectbox('Select the option', config.PAGE)

# condition filtering
if page == "Predict":
    predict()
else:
    explore()

