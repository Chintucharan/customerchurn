import EDA-analysis
# MODULE 2: OBJECTIVE-BASED INSIGHTS
def objective_insights_module(df):
    print("\nOBJECTIVE THAT I HAVE SPECIFICALLY CHOOSEN TO PERFORM IN THIS PROJECT")
# OBJ-1
    print("\nObjective 1: Why Customers Leave Based on Age, Balance, and Credit Score")
    for col in ['Age', 'Balance', 'CreditScore']:
        plt.figure()
        sns.histplot(data=df, x=col, hue='Exited', kde=True, multiple="stack")
        plt.title(f"{col} Distribution by Churn")
        plt.tight_layout()
        plt.show()
#OBJ-2
    print("\nObjective 2: Churn Rate Comparison by Gender")
    plt.figure()
    sns.countplot(data=df, x='Gender', hue='Exited')
    plt.title("Churn Count by Gender")
    plt.tight_layout()
    plt.show()
#OBJ-3
    print("\nObjective 3: Churn Rate Comparison by Country")
    plt.figure()
    sns.countplot(data=df, x='Geography', hue='Exited')
    plt.title("Churn Count by Geography")
    plt.tight_layout()
    plt.show()
#OBJ-4
    print("\nObjective 4: Churn Rate by Age Group")
    df['AgeGroup'] = pd.cut(df['Age'], bins=[18, 30, 40, 50, 60, 100],
                            labels=["18-30", "31-40", "41-50", "51-60", "60+"])
    plt.figure()
    sns.countplot(data=df, x='AgeGroup', hue='Exited')
    plt.title("Churn Count by Age Group")
    plt.tight_layout()
    plt.show()
#OBJ-5 customer trends and risks
    print("\nObjective 5.1: Spending Habits of Churned vs Loyal Customers")
    plt.figure()
    sns.boxplot(data=df, x='Exited', y='EstimatedSalary')
    plt.title("Estimated Salary by Churn")
    plt.tight_layout()
    plt.show()
    print("\nObjective 5.2: Identify Key Factors Linked to Churn")
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap with Churn")
    plt.tight_layout()
    plt.show()
    print("\n Objective 5.3: Summary of Customer Trends and Risk Factors")
    print(
        """These are insights that I have concluded from this project
    Key Insights:
    Older customers (especially those above 50) tend to churn more.
    Customers with high balances but low credit scores are likely to churn more.
    Churn is slightly higher among female customers and those in France.
    Salaries are also a factor and lower earners tends to churn more.
    """)
    #press 2 to to view the objectives
