import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="AI Automation Dashboard", layout="wide")

st.title("🤖 AI Business Automation Dashboard")

# Upload file
uploaded_file = st.file_uploader("Upload Excel or CSV file", type=["csv", "xlsx"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data.csv")

st.write("### 📊 Business Data")
st.dataframe(df)

# Charts
st.write("### 📈 Sales & Profit Chart")
st.line_chart(df.set_index("Date")[["Sales", "Profit"]])

# AI Prediction
st.write("### 🔮 AI Sales Prediction")

X = [[i] for i in range(len(df))]
y = df["Sales"]

model = LinearRegression()
model.fit(X, y)

future_days = st.slider("Predict Future Days", 1, 10)
future_X = [[len(df) + i] for i in range(future_days)]
future_sales = model.predict(future_X)

st.write("Future Sales Prediction:")
st.write(future_sales)

# Plot prediction
plt.figure()
plt.plot(df["Sales"], label="Past Sales")
plt.plot(range(len(df), len(df)+future_days), future_sales, label="AI Prediction")
plt.legend()
st.pyplot(plt)
