# MAIN EXECUTION

import pandas as pd
from objective import objective_insights_module
import EDA_analysis  # make sure this file has a function run_eda(df)

def main():
    print("========== Bank Customer Churn Analysis ==========")
    print("Choose a Module to Run:\n1 - EDA Analysis\n2 - Churn Insights & Objectives")
    choice = input("Enter 1 or 2: ")

    # Load dataset
    df = pd.read_csv("Bank_Churn.csv")  # relative path

    if choice == '1':
        # Run EDA module
        EDA_analysis.run_eda(df)
    elif choice == '2':
        # Run Objective Insights module
        objective_insights_module(df)
    else:
        print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
