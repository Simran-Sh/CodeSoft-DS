
# 💳 Credit Card Fraud Detection using Machine Learning  
**Internship Project – CodeSoft (Nov - Dec 2025 Batch)**  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Imbalanced Data](https://img.shields.io/badge/Imbalanced%20Data-SMOTE-red)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Google%20Colab-yellow)

**Project By:** Simran Sharma  

---


## 📑 Table of Contents

1. [Project Objective](#-project-objective)  
2. [Project Goals](#-project-goals)  
3. [Dataset Description](#-dataset-description)  
4. [Tools & Libraries Used](#-tools--libraries-used)  
5. [Project Workflow](#-project-workflow)  
6. [Model Evaluation & Results](#-model-evaluation--results)  
7. [Threshold Optimization](#-threshold-optimization)  
8. [Model Saving & Deployment Readiness](#-model-saving--deployment-readiness)  
9. [Screenshots & Visuals](#-screenshots--visuals)  
10. [Final Summary](#-final-summary)

---

## 📌 Project Objective

The objective of this project is to build, evaluate, and optimize a machine learning model capable of identifying fraudulent credit card transactions. The project focuses on handling highly imbalanced data and selecting an optimal decision threshold aligned with real-world business costs

---

## 🎯 Project Goals

- Identify fraudulent transactions with high precision and recall  
- Handle extreme class imbalance effectively  
- Compare multiple machine learning models  
- Evaluate models using business-relevant metrics  
- Optimize probability thresholds for real-world deployment  
- Create a reusable and deployment-ready ML pipeline  

---

## 📊 Dataset Description

**Source:** Kaggle – Credit Card Fraud Dataset  
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud  

**Dataset Size:**  
- 120,901 transactions  (in rows)
- 31 total features  (in columns)

**Target Variable:**  
- `Class = 0` → Genuine transaction  
- `Class = 1` → Fraudulent transaction  

**Features:**  
- `Time`: Time elapsed between transactions  
- `V1 – V28`: PCA-transformed anonymized features  
- `Amount`: Transaction amount  

⚠️ **Key Challenge:**  
Fraud cases represent only ~0.2% of the dataset, making it a highly imbalanced classification problem.

---
## 🛠️ Tools & Libraries Used

| Category | Tools / Libraries |
|-------|------------------|
| Programming Language | Python |
| Environment | Google Colab |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Imbalance Handling | Imbalanced-learn (SMOTE) |
| Model Persistence | Joblib |

---

## 🔄 Project Workflow & Explanation

### 1️⃣ Data Loading & Inspection

The dataset was loaded and explored to understand feature structure, data types, and class distribution. This step ensured early identification of data quality issues and confirmed the imbalance problem.

---

### 2️⃣ Train–Test Split (Stratified)

A stratified train-test split was used to preserve the original fraud-to-genuine ratio in both datasets.

**Why required:**  
Prevents biased evaluation caused by uneven class distribution in the test set.

---

### 3️⃣ Feature Scaling (Time & Amount)

Only the `Time` and `Amount` features were scaled.

![Feature scaling](Images\time&amount_FeatureScale.png)

**Why required:**  
- Other features were already PCA-normalized  
- Scaling prevents dominance of large numerical values  
- Improves model convergence and stability  

---

### 4️⃣ Baseline Model 1: Logistic Regression

Logistic Regression was used as a baseline model.

**Purpose:**  
- Simple and interpretable  
- Acts as a benchmark for comparison  

**Observation:**  
- Very high recall for fraud  
- Extremely low precision  
- Many false positives  

**Conclusion:**  
Good for detecting fraud but operationally expensive due to false alerts.

---

### 5️⃣ Baseline Model 2: Random Forest

Random Forest was selected due to its ability to model non-linear relationships.

**Advantages:**  
- Handles imbalance better  
- Robust to noise  
- Strong generalization performance  

**Result:**  
Significant improvement in precision, recall, and F1-score compared to logistic regression.

---

### 6️⃣ Handling Class Imbalance using SMOTE

SMOTE (Synthetic Minority Oversampling Technique) was applied during training.

**Why required:**  
- Generates synthetic fraud samples  
- Prevents bias toward majority class  
- Improves minority class learning  

**Outcome:**  
More balanced recall–precision trade-off.

---

### 7️⃣ Model Evaluation Metrics

Accuracy alone was avoided due to class imbalance. The following metrics were used:

- **Precision:** Correctness of fraud predictions  
- **Recall:** Ability to detect actual fraud  
- **F1-Score:** Balance between precision and recall  
- **ROC-AUC:** Overall class separability  
- **Average Precision (AP):** Performance under imbalance  

---

### 8️⃣ ROC & Precision–Recall Curve Comparison

Visual comparisons helped evaluate trade-offs between recall and false positives.

![ROC & Precision–Recall Curve Comparison](Images\CurveComparison_ROC&PrecisionRecall.png)

**Why important:**  
Missing fraud is costlier than flagging genuine transactions.

---

### 9️⃣ Threshold Optimization (Business-Centric)

Multiple probability thresholds were evaluated instead of using the default 0.5.

![Threshold = 0.5](Images\Threshold_1.png)
![Threshold = 0.3](Images\Threshold_2.png)
![Threshold = 0.2](Images\Threshold_3.png)
![Threshold = 0.1](Images\Threshold_4.png)

**Approach:**  
- Tested multiple thresholds  
- Calculated expected business cost  
- Selected threshold with minimum cost  

**Best Threshold:** `0.14`  
**Minimum Expected Cost:** `2380`  

![Threshold by Business Cos](Images\Threshold_5.png)

---

### 🔟 Hyperparameter Tuning & Cross-Validation

Grid Search with cross-validation was used to:

- Identify optimal hyperparameters  
- Reduce overfitting  
- Improve model robustness  

The best estimator was selected for final evaluation.

---

### 1️⃣1️⃣ Final Model Evaluation

The tuned Random Forest model demonstrated:

- High fraud detection capability  
- Strong generalization on unseen data  
- Excellent precision-recall balance  

Confusion matrices and probability analysis validated real-world usability.

---

### 1️⃣2️⃣ Model Saving & Reusability

The final trained model was saved using Joblib.

**Why required:**  
- Enables deployment  
- Allows future inference without retraining  
- Supports production-level workflows  

---

## 📈 Key Results Summary

- Random Forest outperformed Logistic Regression  
- SMOTE improved fraud detection stability  
- Threshold optimization reduced business cost  
- Average Precision ≈ 0.90  
- Very low false-negative rate  

---

## ✅ Final Conclusion

This project demonstrates a complete end-to-end machine learning workflow for fraud detection, covering data preprocessing, imbalance handling, model comparison, evaluation, optimization, and deployment readiness. The final solution balances technical performance with real-world business considerations, making it suitable for practical fraud detection systems.

---

### 📌 Internship Final Project Submission
**Organization:** CodeSoft  
**Batch:** Nov - Dec 2025  
**Project Type:** Machine Learning Classification  

