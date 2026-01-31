# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import importlib
import src.config as config

importlib.reload(config)

@st.cache_data
def load_data():
    df = pd.read_csv(config.DATA_PATH)

    salary_df = pd.DataFrame(df.groupby('Country')['Salary'].mean().reset_index())
    salary_df = salary_df.sort_values(by='Salary', ascending=False)
    salary_df['Salary'] = round(salary_df['Salary'], 2)
    country_df = pd.DataFrame(df['Country'].value_counts().reset_index())
    
    return df, salary_df, country_df