# -*- coding: utf-8 -*-

import streamlit as st
import re
import importlib
import src.config as config
importlib.reload(config)

def UI_inputs():
    employee_name = st.text_input('Enter the name')
    
    if employee_name == "":
        st.error("Name is required.")
    elif not re.match("^[A-Za-z ]+$", employee_name):
        st.error("Name should contain only letters and spaces.")
    else:
        pass

    age = st.number_input('Enter the age', min_value=18, max_value=65, step=1, format="%d")
    
    if age is not None:
        if age < 18:
            st.error('AgeError, please enter valid age')
         
    edlevel = st.selectbox('Select education level', config.ED_LEVEL)
    
    country = st.selectbox('Select Country', config.COUNTRIES)
    
    employment = st.selectbox('Select Employment_status', config.EMPLOYMENT)
    
    work_exp = st.number_input('Enter the YOE', 0, step=1, format="%d")
    
    if work_exp is not None:
        if work_exp < 0:
            st.error('Error, please enter valid YOE')

        if work_exp > (age - 18):
            st.error('Error, Please enter valid YOE')
    
    job_sat = st.slider('Job satisfaction', min_value=0, max_value=10)
    
    ui_inputs = {
            'Age' : age,
            'EdLevel' : edlevel,
            'Employment' : employment,
            'Country' : country,
            'WorkExp' : work_exp,
            'JobSat' : job_sat
            }
    
    return ui_inputs