# -*- coding: utf-8 -*-

import plotly.express as px
import streamlit as st

def plot_visualization(df_country, salary_df, edlvl_df):
    
    #pie chart
    fig1 = px.pie(data_frame=df_country, names='Country', values='count', hover_data='count',
                  title='No of software developers from each country in 2025')

    fig1 = st.plotly_chart(fig1, use_container_width=True) # storing the pie chart

    # bar chart for top 10 countries
    fig2 = px.bar(data_frame=salary_df.head(10), x='Salary', y='Country', color = 'Salary',
                  title='Top 10 Countries with highly earning software developers (in $) in 2025',
                  color_continuous_scale="Viridis")
    fig2.update_layout(yaxis=dict(autorange="reversed"))

    fig2 = st.plotly_chart(fig2, use_container_width=True)  # storing the bar chart

    # bar chart for bpttom 10 countries
    fig3 = px.bar(data_frame=salary_df.tail(10), x='Salary', y='Country', color='Salary', 
                  color_continuous_scale="Viridis",
                  title='Bottom 10 Countries with the lower mean salary for software developers (in $) in 2025')

    fig3 = st.plotly_chart(fig3, use_container_width=True) # storing the bar chart

    # choropleth plot using world map
    fig4 = px.choropleth(salary_df, locations="Country", locationmode="country names",
                     color="Salary", color_continuous_scale="Viridis", title="Mean Salary by Country")

    fig4 = st.plotly_chart(fig4, use_container_width=True) # storing the choropleth plot

    # bar chart for mean salary as per the education levels
    fig5 = px.bar(data_frame=edlvl_df, x='Salary', y='EdLevel', color = 'Salary',
                  title='The mean salary for software developers (in $) in 2025 as per the education level',
                  color_continuous_scale="Viridis")
    fig5.update_layout(yaxis=dict(autorange="reversed"))

    fig5 = st.plotly_chart(fig5, use_container_width=True) # storing the pie chart
    
    return fig1, fig2, fig3, fig4, fig5




