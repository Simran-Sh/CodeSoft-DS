
# Titanic_Prediction_Project deployed on streamlit **[🔗 Try the App Now!](https://titanicpredictionproject-codsoftinternshipp.streamlit.app/)**
CodeSoft Internship Project 1

## Project Overview
 This was a Mchine learning project to predict whether a passenger on the Titanic survived or not using the famous Titanic dataset from Kaggle 

 ## Data Set
 | **Source** | **[Titanic Dataset by YasserH](https://www.kaggle.com/datasets/yasserh/titanic-dataset)** |
|------------|---------------------------------------------------------------------------------------|

 Description
 - **Source**: Titanic dataset (publicly available)
- **Rows**: 891 passenger records
- **Columns**: 12 columns, including:
  - PassengerId: Unique ID for each passenger
  - Survived: Target variable (0 = Did not survive, 1 = Survived)
  - Pclass: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)
  - Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked

---

## Exploratory data analysis
**Data cleaning and preprocessing included:**
- Dropping irrelevant columns like `Name`, `Ticket`, and `Cabin`
- Filling missing `Age` values with median age
- Filling missing `Embarked` values with mode
- Encoding categorical variables (`Sex`, `Embarked`) via one-hot encoding

---

## Development Workflow

### Step 1: Data Exploration & Model Building in Google Colab

- Load dataset CSV into pandas
- Perform exploratory data analysis to understand data quality and distributions
- Clean data by handling missing values
- Convert categorical variables to numeric via one-hot encoding
- Train a Logistic Regression model using `scikit-learn` with train-test split
- Achieved an accuracy of approximately 80.4%
- Save the trained model locally as `titanic_model.pkl`
- Download the model file from Colab to local machine

### Step 2: Local Development - Virtual Environment Setup

- Create a project folder locally (e.g., `Titanic_Prediction_Project`)
- Move the downloaded `titanic_model.pkl` file into this folder
- Open Command Prompt (Windows Terminal) and navigate to the project folder
- Create and activate a Python virtual environment:

- Upgrade `pip` and install necessary libraries:


### Step 3: Building the Streamlit App in VS Code

- **Use VS Code** to open the project folder (`E:\Titanic_Prediction_Project`)
- **Create** `app.py` in the folder
- **Develop the Streamlit app that:**
  - 🔄 **Loads the saved model** (`titanic_model.pkl`) using `joblib`
  - 🎛️ **Provides input widgets** for passenger features:
    | Widget | Feature |
    |--------|---------|
    | `number_input` | Passenger ID |
    | `selectbox` | Pclass (1,2,3), Sex, Embarked |
    | `slider` | Age, SibSp, Parch, Fare |
  - 🧹 **Processes input features** with **same preprocessing as training**:
    - Fill missing Age with median
    - One-hot encode Sex, Embarked (`drop_first=True`)
    - Match exact column order: `['PassengerId', 'Pclass', 'Age', ...]`
  - 🎯 **Predicts survival** with model, showing:
    - ✅ **Result**: "Survived" or "Did Not Survive"
    - 📊 **Probabilities**: Survival % + Death %

**Code handles edge cases automatically** - exact feature matching with training data!

### Step 4: Running the App Locally

- Run the Streamlit app in terminal:
    - I was able to interact with the UI and get survival prediction in real time without needing the dataset
 
### Step 5: Deploy on Streamlit 
- Created repo on github
- Deplyed project on streamlit using the repo 

---

## Project Outcome

- Completed end-to-end ML project from data cleaning to deployment
- Gained practical experience working with real-world dataset and production tools
- Developed strong skills in data preprocessing, model training, and Python-based web app development
- Demonstrated ability to deliver a working, interactive application for real users

---

## ✨ **Live Demo**
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://titanicpredictionproject-codsoftinternshipp.streamlit.app/)

**[🔗 Try the App Now!](https://titanicpredictionproject-codsoftinternshipp.streamlit.app/)**

**80.4% Accuracy Model** | **Interactive Predictions** | **Deployed on Streamlit Cloud**

---

## How to Run This Project

1. Clone this repository.
2. Create and activate virtual environment.
3. Install dependencies:
    pip install -r requirements.txt
4. Run the app 


