import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Load your trained model (save it first from notebook)
# In notebook: pickle.dump(lin_reg, open('model.pkl', 'wb'))
@st.cache_resource
def load_model():
    return pickle.load(open('model.pkl', 'rb'))

st.title("📈 Sales Prediction Dashboard")
st.write("Predict sales based on TV, Radio, Newspaper ad spend")

# Input sliders
col1, col2, col3 = st.columns(3)
with col1:
    tv = st.slider("TV Ad Spend ($K)", 0.0, 300.0, 150.0)
with col2:
    radio = st.slider("Radio Ad Spend ($K)", 0.0, 50.0, 25.0)
with col3:
    newspaper = st.slider("Newspaper Ad Spend ($K)", 0.0, 120.0, 20.0)

# Predict
if st.button("🚀 Predict Sales"):
    model = load_model()
    input_data = np.array([[tv, radio, newspaper]])
    prediction = model.predict(input_data)[0]
    st.success(f"**Predicted Sales: ${prediction:.2f}K**")
    
    # ROI insights
    st.metric("TV ROI", "Best ($0.046/sales per $)")
    st.metric("Radio ROI", "Good ($0.197/sales per $)")
    st.metric("Newspaper ROI", "Poor ($0.003/sales per $)")

# Dataset preview
st.subheader("📊 Sample Data")
df = pd.read_csv('advertising.csv')
st.dataframe(df.head())
st.write("Dataset contains ad spends and sales figures.")