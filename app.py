import pandas as pd
import streamlit as st

st.title("IoT Sensor Dashboard")

# Read data from CSV file
df = pd.read_csv("sensor.csv")

st.subheader("Sensor Data")
st.dataframe(df)

# Get the latest values without using iloc (using NumPy array indexing)
latest_temp = df["Temperature"].values[-1]
latest_humid = df["Humidity"].values[-1]

st.metric("Temperature", f"{latest_temp} °C")
st.metric("Humidity", f"{latest_humid}%")

# Alternatively, you can use st.line_chart or st.bar_chart directly
st.subheader("Temperature Chart")
st.bar_chart(df, x="Time", y="Temperature")
