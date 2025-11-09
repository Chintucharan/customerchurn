import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def objective_insights_module(df, use_streamlit=False):
    if use_streamlit:
        st.subheader("Objective 1: Why Customers Leave Based on Age, Balance, and Credit Score")
    for col in ['Age', 'Balance', 'CreditScore']:
        plt.figure()
        sns.histplot(data=df, x=col, hue='Exited', kde=True, multiple="stack")
        plt.title(f"{col} Distribution by Churn")
        if use_streamlit:
            st.pyplot(plt)
        else:
            plt.show()
        plt.close()

    if use_streamlit:
        st.subheader("Objective 2: Churn Rate Comparison by Gender")
    plt.figure()
    sns.countplot(data=df, x='Gender', hue='Exited')
    if use_streamlit:
        st.pyplot(plt)
    else:
        plt.show()
    plt.close()

    if use_streamlit:
        st.subheader("Objective 3: Churn Rate Comparison by Country")
    plt.figure()
    sns.countplot(data=df, x='Geography', hue='Exited')
    if use_streamlit:
        st.pyplot(plt)
    else:
        plt.show()
    plt.close()

    if use_streamlit:
        st.subheader("Objective 4: Churn Rate by Age Group")
    df['AgeGroup'] = pd.cut(df['Age'], bins=[18,30,40,50,60,100],
                            labels=["18-30","31-40","41-50","51-60","60+"])
    plt.figure()
    sns.countplot(data=df, x='AgeGroup', hue='Exited')
    if use_streamlit:
        st.pyplot(plt)
    else:
        plt.show()
    plt.close()

    if use_streamlit:
        st.subheader("Objective 5.1: Spending Habits of Churned vs Loyal Customers")
    plt.figure()
    sns.boxplot(data=df, x='Exited', y='EstimatedSalary')
    if use_streamlit:
        st.pyplot(plt)
    else:
        plt.show()
    plt.close()

    if use_streamlit:
        st.subheader("Objective 5.2: Correlation Heatmap")
    plt.figure(figsize=(10,8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    if use_streamlit:
        st.pyplot(plt)
    else:
        plt.show()
    plt.close()

    if use_streamlit:
        st.subheader("Objective 5.3: Summary of Customer Trends and Risk Factors")
        st.write("""
Key Insights:
- Older customers (especially those above 50) tend to churn more.
- Customers with high balances but low credit scores are more likely to churn.
- Churn is slightly higher among female customers and those in France.
- Lower salaries also tend to correlate with higher churn.
""")
