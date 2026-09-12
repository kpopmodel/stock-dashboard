import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

st.title("테스트 3: pandas + plotly만 (st.dataframe 제외)")

dates = pd.date_range("2026-01-01", periods=30)
df = pd.DataFrame({
    "Open": np.random.randint(1700, 1900, 30),
    "High": np.random.randint(1800, 1950, 30),
    "Low": np.random.randint(1650, 1800, 30),
    "Close": np.random.randint(1700, 1900, 30),
}, index=dates)

fig = go.Figure(data=[go.Candlestick(
    x=df.index, open=df["Open"], high=df["High"], low=df["Low"], close=df["Close"],
)])
st.plotly_chart(fig, use_container_width=True)

st.write("여기까지 잘 보이면 st.dataframe(표)이 범인, plotly/pandas는 무죄")
