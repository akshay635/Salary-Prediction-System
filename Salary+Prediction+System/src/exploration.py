# -*- coding: utf-8 -*-
# exploration.py

from src.load_data import load_data
from src.plot_visualizations import plot_visualization
import streamlit as st

def explore():
    
    df, salary_df, country_df, edlevel_df = load_data()
    
    f1, f2, f3, f4, f5 = plot_visualization(country_df, salary_df, edlevel_df)

    col1, col2 = st.columns(2)
    
    return f1
    
    with col1:
        return f2

    with col2:
        return f3

    return f4, f5
        
    
    

    


