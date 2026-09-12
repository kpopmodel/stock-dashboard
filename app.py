import streamlit as st
import pandas as pd
import numpy as np

st.title("테스트 4: pandas + numpy만 (plotly 제외)")

dates = pd.date_range("2026-01-01", periods=30)
df = pd.DataFrame({
    "Open": np.random.randint(1700, 1900, 30),
    "Close": np.random.randint(1700, 1900, 30),
}, index=dates)

st.write(f"데이터 shape: {df.shape}")
st.write(f"평균 종가: {df['Close'].mean()}")

st.write("여기까지 잘 보이면 pandas/numpy는 무죄, plotly가 범인")
