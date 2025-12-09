import streamlit as st
import joblib
import pandas as pd

# Load model
@st.cache_resource
def load_model():
    return joblib.load('titanic_model.pkl')

model = load_model()

st.title("🛳️ Titanic Survival Predictor")

# Input widgets
passenger_id = st.number_input("Passenger ID", 1, 891, 1)
pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 80, 28)
sibsp = st.slider("Siblings/Spouses", 0, 8, 0)
parch = st.slider("Parents/Children", 0, 6, 0)
fare = st.slider("Fare", 0.0, 500.0, 14.45)
embarked = st.selectbox("Embarked", ["C", "Q", "S"])

# Create input dataframe - EXACT training columns
input_data = pd.DataFrame({
    'PassengerId': [passenger_id],
    'Pclass': [pclass],
    'Sex': [sex],
    'Age': [age],
    'SibSp': [sibsp],
    'Parch': [parch],
    'Fare': [fare],
    'Embarked': [embarked]
})

# SAME preprocessing as training
input_data['Age'].fillna(input_data['Age'].median(), inplace=True)
input_data = pd.get_dummies(input_data, columns=['Sex', 'Embarked'], drop_first=True)

# EXACT column order from your model
required_cols = ['PassengerId', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex_male', 'Embarked_Q', 'Embarked_S']
for col in required_cols:
    if col not in input_data.columns:
        input_data[col] = 0
input_data = input_data[required_cols]

if st.button("🚀 Predict Survival"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]
    
    st.success("**Prediction:** " + ("✅ Survived" if prediction == 1 else "❌ Did Not Survive"))
    st.info(f"**Survival Probability:** {probability[1]:.1%}")
    st.info(f"**Death Probability:** {probability[0]:.1%}")
