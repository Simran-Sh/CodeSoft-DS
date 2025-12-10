# Sales Prediction using Machine Learning 📈

**CodeSoft Data Science Internship - Project 2**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.14](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

## 🎯 **Project Objective**

Build a **Multiple Linear Regression** model to predict **sales** based on advertising spend across **TV, Radio, and Newspaper** channels. This helps businesses optimize their advertising budget allocation.

**Business Problem**: How much will sales increase if we spend $1 more on TV vs Radio vs Newspaper ads?

---

## 📋 **Key Goals**

- ✅ Load and explore advertising dataset (200 observations)
- ✅ Perform Exploratory Data Analysis (EDA) with visualizations
- ✅ Build Linear Regression model: `Sales = β₀ + β₁TV + β₂Radio + β₃Newspaper`
- ✅ Evaluate model performance (RMSE, R²)
- ✅ Interpret business insights from model coefficients

---

## 🛠️ **Tech Stack & Environment**

| Tool/Library | Purpose |
|--------------|---------|
| **VS Code** + Jupyter Extension | Interactive notebook development |
| **pandas** | Data loading & manipulation |
| **numpy** | Numerical computations |
| **matplotlib + seaborn** | EDA visualizations |
| **scikit-learn** | ML modeling & evaluation |

### Quick Setup

---

## 📊 **Dataset Overview**

| Feature | Description | Range |
|---------|-------------|-------|
| **TV** | TV advertising spend ($) | 0.7 - 296.4 |
| **Radio** | Radio advertising spend ($) | 0.0 - 49.6 |
| **Newspaper** | Newspaper advertising spend ($) | 0.3 - 114.0 |
| **Sales** | Product sales ($) **← Target** | 1.6 - 27.0 |

**Key Insight**: TV & Radio have strong linear relationship with Sales. Newspaper shows weak correlation.

---

## 🚀 **Complete Workflow**

### 1. **Data Loading & Exploration**
### 2. **Exploratory Data Analysis (EDA)**
### 3. **Model Building**

### 4. **Model Evaluation**
| Metric | Value | Interpretation |
|--------|-------|----------------|
| **R²** | ~0.90 | 90% of sales variance explained |
| **RMSE** | ~1.8 | Average prediction error: ±$1.8K |

### 5. **Business Insights**

**Recommendation**: Allocate 60% budget to TV, 35% to Radio, 5% to Newspaper.

---

## 🔍 **Key Learning Points**

1. **random_state=42**: Ensures **same train/test split every run** → Essential for teaching/debugging
2. **print(sys.executable)**: Shows **exact Python path** your notebook uses
3. **!{sys.executable} -m pip install**: Installs packages to **notebook's environment**
4. **Coefficients (β)**: Show marginal impact of each ad channel on sales

---

## 🐛 **Troubleshooting**

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'sklearn'` | `!{sys.executable} -m pip install scikit-learn` |
| VS Code kernel wrong Python | `Ctrl+Shift+P` → "Python: Select Interpreter" |
| Plots not showing | `%matplotlib inline` at notebook start |

---





