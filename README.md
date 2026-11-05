# 🏦 Bank Customer Churn Analysis

> End-to-end exploratory analysis of 10,000 bank customers to find **who leaves, why, and which segments to target first** with retention campaigns.

**Tools:** Python · Pandas · NumPy · Matplotlib · Seaborn · scikit-learn · Jupyter
**Dataset:** [Maven Analytics – Bank Churn](https://mavenanalytics.io/data-playground) (10,000 customers, 14 columns)
**Context:** INT375 – Data Science Toolbox: Python Programming, Lovely Professional University (Jan–Apr 2025)
**Author:** Gowni Venkat Charan · [LinkedIn](https://www.linkedin.com/in/gowni-venkat-charan-1b06562a8) · [GitHub](https://github.com/Chintucharan/customerchurn)

---

## 📌 Business Problem

Acquiring a new customer costs far more than keeping an existing one. This project answers:

1. Which customers are most likely to churn?
2. How do age, geography, gender, balance and credit score relate to churn?
3. Do product usage and engagement (active membership, tenure, credit card) predict churn?
4. Can churn risk be predicted, and what should the bank do about it?

## 🗂️ Dataset

| Group | Columns |
|---|---|
| Identifiers | `RowNumber`, `CustomerId`, `Surname` |
| Demographics | `Age`, `Gender`, `Geography` (France / Germany / Spain) |
| Financial | `CreditScore`, `Balance`, `EstimatedSalary` |
| Behavioral | `Tenure`, `NumOfProducts`, `HasCrCard`, `IsActiveMember` |
| Target | `Exited` (1 = churned, 0 = retained) |

## 🔧 Workflow

1. **Data loading & inspection** – `read_csv`, `head()`, `info()`
2. **Data quality checks** – null values, duplicates
3. **Descriptive statistics** – `describe()`
4. **Correlation & covariance** – heatmap of all numeric features; covariance of CreditScore, Age, Balance, EstimatedSalary
5. **Outlier detection** – horizontal boxplots on CreditScore, Age, Balance
6. **Relationship exploration** – pairplot of CreditScore, Age, Balance, EstimatedSalary coloured by `Exited` (500-row sample)
7. **Objective-based analysis** – 5 business questions (below)
8. **Churn prediction** – logistic regression & decision tree baseline

## 🔍 Analysis Objectives

| # | Objective | Techniques | Visuals |
|---|---|---|---|
| 1 | Churn by age, balance, credit score | `pd.cut()` age bins, `groupby().mean()` | Bar chart, boxplot, histogram |
| 2 | Churn by gender & geography | `groupby()['Exited'].mean()` | Countplot, bar chart |
| 3 | Salary & product usage: churned vs. loyal | `groupby()`, `value_counts()` | Boxplot, countplot |
| 4 | Tenure, activity status, credit card | Filtering, churn-rate formulas | Line plot, countplots |
| 5 | Predict churn risk | Logistic regression, decision tree | Feature importance, ROC curve |

**Churn rate** = `Exited customers ÷ Total customers × 100`


## 📊 Key Findings

> ⚠️ Fill in the exact figures from your notebook output before publishing (see *Verify before publishing* below).

- **Age is the strongest single driver.** Churn rises sharply through the 40s and 50s; older customers are far more likely to leave than customers under 35.
- **Inactive members churn at roughly twice the rate** of active members → engagement is a leading indicator.
- **Geography matters.** Compare France, Germany and Spain churn rates from your output: `France __%`, `Germany __%`, `Spain __%`.
- **Gender gap:** female customers churn at a higher rate than male customers (`__%` vs `__%`).
- **Product count is non-linear.** Customers with 1 product and customers with 3+ products behave very differently from those with 2 → check `groupby('NumOfProducts')['Exited'].mean()`.
- **Balance:** churned customers hold higher average balances, meaning the bank is losing high-value customers.
- **Salary and credit card ownership** show little difference between churned and retained groups.
- **Baseline model accuracy ≈ 85%**; report precision, recall and ROC-AUC as well, since only ~20% of customers churn.

## 💡 Recommendations

1. Launch retention outreach for **inactive customers aged 40+** with high balances.
2. Create engagement triggers (offers, calls) for customers whose activity drops.
3. Review the product bundle for customers with 1 or 3+ products.
4. Investigate the highest-churn country for local service or pricing issues.
5. Score customers monthly with the churn model and prioritise by balance × risk.

## 🚀 How to Run

```bash
git clone https://github.com/Chintucharan/customerchurn.git
cd customerchurn
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
python churn_eda.py
```

Place `Bank_Churn.csv` in the project folder first. The EDA script prints null/duplicate checks and the covariance matrix, and displays the heatmap, boxplot and pairplot. The objective-based analysis and churn model are in `churn_analysis.ipynb`.

## 📁 Repository Structure

```
├── Bank_Churn.csv
├── churn_eda.py         # Module 1: EDA
├── churn_analysis.ipynb # Module 2: objective-based analysis & model
├── README.md
└── report.pdf
```

## 🔮 Future Work

- Real-time churn scoring with live account activity
- Customer segmentation (e.g., "high-value but at-risk") using clustering
- Interactive Tableau / Power BI dashboard
- Cross-sell and upsell targeting
- Sentiment analysis on complaints and feedback
- Class-imbalance handling (SMOTE, class weights) and gradient boosting models

## 🧠 Skills Demonstrated

`Data cleaning` · `EDA` · `Statistical analysis` · `Data visualization` · `Feature analysis` · `Churn / KPI metrics` · `Classification modelling` · `Business storytelling`

## 👤 Author

**Gowni Venkat Charan**
[LinkedIn](https://www.linkedin.com/in/gowni-venkat-charan-1b06562a8) · [GitHub](https://github.com/Chintucharan)
