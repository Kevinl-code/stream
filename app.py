import pandas as pd
import streamlit as st

st.title("IoT Sensor Dashboard")

df = pd.read_csv("sensor.csv")

st.subheader("Sensor Data")
st.dataframe(df)

latest_temp = df["Temperature"].values[-1]
latest_humid = df["Humidity"].values[-1]

st.metric("Temperature", f"{latest_temp} °C")
st.metric("Humidity", f"{latest_humid}%")
st.subheader("Temperature Chart")
st.bar_chart(df, x="Time", y="Temperature")
