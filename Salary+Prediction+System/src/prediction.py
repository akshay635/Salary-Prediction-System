# -*- coding: utf-8 -*-
# prediction.py

import streamlit as st
import pandas as pd
import numpy as np
from src.load_models import load_model
from src.load_inputs import UI_inputs

def predict():
    
    model, preprocessor = load_model()
    
    user_inputs = UI_inputs()
    
    if st.button('Predict The Salary'):
        df = pd.DataFrame([user_inputs])
        for col in ['EdLevel', 'Employment', 'Country']:
            df[col] = df[col].astype('category')

        df = preprocessor.transform(df)
        pred = model.predict(df)
        pred_transform = np.expm1(pred)
        st.success(f'Predicted Salary of Employee is ${pred_transform[0]:.2f}')
    
    
    
    
    
    
    