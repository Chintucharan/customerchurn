# 🏦 Bank Customer Churn Analysis

**Python · Pandas · NumPy · Matplotlib · Seaborn · scikit-learn**

An end-to-end analysis of 10,000 bank customers to understand **who churns, why, and which segments the bank should target first**. The project covers data cleaning, exploratory analysis, five business-driven questions, a baseline prediction model, and actionable retention recommendations.

**Author:** Gowni Venkat Charan · [LinkedIn](https://www.linkedin.com/in/gowni-venkat-charan-1b06562a8) · [GitHub](https://github.com/Chintucharan/customerchurn)

---

## 📌 Business Problem

Retaining a customer is cheaper than acquiring a new one. This analysis answers:

1. Which customer segments are most likely to leave?
2. How do age, geography, gender, balance and credit score relate to churn?
3. Do product holdings and engagement (activity, tenure, credit card) signal risk?
4. Can churn be predicted well enough to act on it?

## 🗂️ Dataset

Source: [Maven Analytics – Bank Churn](https://mavenanalytics.io/data-playground) · **10,000 rows × 14 columns** · overall churn rate ≈ **20%**

| Group | Columns |
|---|---|
| Identifiers | `RowNumber`, `CustomerId`, `Surname` |
| Demographics | `Age`, `Gender`, `Geography` (France, Germany, Spain) |
| Financial | `CreditScore`, `Balance`, `EstimatedSalary` |
| Behavioral | `Tenure`, `NumOfProducts`, `HasCrCard`, `IsActiveMember` |
| Target | `Exited` (1 = churned, 0 = retained) |

## 🔧 Approach

1. **Data quality** – checked nulls and duplicates (no missing values found)
2. **Descriptive statistics** – mean age ≈ 39, mean balance ≈ 76K, credit scores 350–850
3. **Correlation & covariance** – heatmap of numeric features; covariance of CreditScore, Age, Balance, EstimatedSalary
4. **Outlier detection** – boxplots of CreditScore, Age, Balance
5. **Relationship exploration** – pairplot (500-row sample) coloured by `Exited`
6. **Objective-based analysis** – five business questions (below)
7. **Modelling** – logistic regression and decision tree baselines

**Churn rate** = `churned customers ÷ total customers × 100`

## 🔍 Objectives & Methods

| # | Question | Methods |
|---|---|---|
| 1 | How do age, balance and credit score relate to churn? | `pd.cut()` age bands, `groupby().mean()`, boxplots, histograms |
| 2 | Does churn differ by gender and country? | `groupby()['Exited'].mean()`, countplot, barplot |
| 3 | Do salary and product usage differ for churned vs. retained customers? | `groupby()`, `value_counts()`, boxplot, countplot |
| 4 | Do tenure, activity status and credit card ownership matter? | Filtered churn rates, line plot, countplots |
| 5 | Can churn risk be predicted? | Logistic regression, decision tree, feature importance, ROC curve |

## 📊 Key Findings

| Factor | Finding |
|---|---|
| **Age** | The strongest numeric signal (correlation with churn ≈ 0.29). Churn is highest for customers in their 50s (over half leave) and much lower under 35. |
| **Geography** | Germany churns most (≈ 32%), roughly double France (≈ 16%) and Spain (≈ 17%). |
| **Gender** | Female customers churn more (≈ 25%) than male customers (≈ 16%). |
| **Activity** | Inactive members churn at ≈ 27% vs ≈ 14% for active members. |
| **Products** | Customers with 2 products are the most loyal (≈ 8% churn). Those with 1 product churn ≈ 28%, and those with 3–4 products churn at very high rates (small group). |
| **Balance** | Churned customers hold higher average balances (≈ 91K vs ≈ 73K), so the bank is losing valuable accounts. |
| **Credit score, salary, credit card, tenure** | Little to no meaningful difference between churned and retained customers. |
| **Prediction** | Baseline models reach roughly 85% accuracy. About 80% of customers do not churn, so accuracy alone is misleading and recall/ROC-AUC matter more. |

> Figures are rounded and come from the analysis in this repository; rerun the code to reproduce them.

## 💡 Recommendations

1. **Target inactive customers aged 40+** with personalised outreach before they leave.
2. **Investigate the German market** (service quality, pricing, competition) given its much higher churn.
3. **Re-engage 1-product customers** with a second product, since 2-product customers are the most loyal.
4. **Review the 3–4 product bundles**, as customers with many products churn unusually often.
5. **Prioritise high-balance, high-risk customers** using model scores for retention budget.
6. **Monitor activity drops monthly** as an early-warning signal.

## ⚠️ Limitations

- Snapshot data with no transaction history, complaints or time dimension, so causes of churn can only be inferred.
- Churn is imbalanced (~20%); future work should use class weighting/SMOTE and report precision, recall and F1.
- Correlation is not causation; findings show association, not proven drivers.

## 🚀 How to Run

```bash
git clone https://github.com/Chintucharan/customerchurn.git
cd customerchurn
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
python churn_eda.py
```

Place `Bank_Churn.csv` in the project folder first. The EDA script prints null/duplicate checks and the covariance matrix, then displays the heatmap, boxplots and pairplot. The objective-based analysis and model are in `churn_analysis.ipynb`.

## 📁 Repository Structure

```
├── Bank_Churn.csv
├── churn_eda.py          # Module 1: EDA
├── churn_analysis.ipynb  # Module 2: objective-based analysis & model
└── README.md
```

## 🔮 Future Work

- Real-time churn scoring from live account activity
- Customer segmentation (e.g., "high-value but at-risk") with clustering
- Gradient boosting models with proper imbalance handling
- Interactive Tableau / Power BI dashboard
- Sentiment analysis of complaints and feedback

## 🧠 Skills Demonstrated

Data cleaning · EDA · Statistical analysis · Data visualization · Churn/KPI metrics · Classification modelling · Business storytelling

## 👤 Author

**Gowni Venkat Charan**
[LinkedIn](https://www.linkedin.com/in/gowni-venkat-charan-1b06562a8) · [GitHub](https://github.com/Chintucharan)
