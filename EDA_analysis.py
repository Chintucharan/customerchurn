import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def run_eda(df, use_streamlit=False):
    if use_streamlit:
        st.subheader("===== EDA ANALYSIS =====")

    if use_streamlit:
        st.subheader("Step 1: Checking for Null Values")
        st.write(df.isnull().sum())
    else:
        print(df.isnull().sum())

    if use_streamlit:
        st.subheader("Step 2: Removing Duplicate Records")
        st.write(f"Duplicates before removal: {df.duplicated().sum()}")
    else:
        print(f"Duplicates before removal: {df.duplicated().sum()}")

    df.drop_duplicates(inplace=True)

    if use_streamlit:
        st.write("Duplicates removed successfully.")
    else:
        print("Duplicates removed successfully.")

    if use_streamlit:
        st.subheader("Step 3: Correlation Heatmap")
    plt.figure(figsize=(10,8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    if use_streamlit:
        st.pyplot(plt)
    else:
        plt.show()
    plt.close()

    cov_columns = ['CreditScore', 'Age', 'Balance', 'EstimatedSalary']
    if use_streamlit:
        st.subheader("Step 4: Covariance Matrix")
        st.write(df[cov_columns].cov())
    else:
        print(df[cov_columns].cov())

    if use_streamlit:
        st.subheader("Step 5: Outlier Detection (Boxplot)")
    plt.figure(figsize=(10,6))
    num_cols = ['CreditScore', 'Age', 'Balance']
    sns.boxplot(data=df[num_cols], orient='h')
    if use_streamlit:
        st.pyplot(plt)
    else:
        plt.show()
    plt.close()

    if use_streamlit:
        st.subheader("Step 6: Pairplot of Key Numerical Features")
    pairplot_columns = ['CreditScore', 'Age', 'Balance', 'EstimatedSalary', 'Exited']
    sampled_df = df.sample(min(500, len(df)), random_state=1)
    pairplot = sns.pairplot(sampled_df[pairplot_columns], hue='Exited')
    if use_streamlit:
        st.pyplot(pairplot.fig)
    else:
        plt.show()
    plt.close()
