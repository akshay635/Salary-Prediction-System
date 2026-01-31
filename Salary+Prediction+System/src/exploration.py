# -*- coding: utf-8 -*-
# exploration.py

from src.load_data import load_data
from src.plot_visualizations import plot_visualization

def explore():
    
    df, salary_df, country_df, employment_df = load_data()
    
    plot_visualization(country_df, salary_df, employment_df)
    
    

    
