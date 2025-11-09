import pandas as pd
import streamlit as st
from EDA_analysis import run_eda
from objective import objective_insights_module

st.title("Bank Customer Churn Analysis")

df = pd.read_csv("Bank_Churn.csv")

choice = st.sidebar.radio("Choose a Module", ["EDA Analysis", "Churn Insights & Objectives"])

if choice == "EDA Analysis":
    st.header("Exploratory Data Analysis (EDA)")
    run_eda(df, use_streamlit=True)

elif choice == "Churn Insights & Objectives":
    st.header("Churn Insights & Objectives")
    objective_insights_module(df, use_streamlit=True)
