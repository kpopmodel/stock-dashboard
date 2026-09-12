import streamlit as st

st.title("테스트 6: pandas만 단독 테스트")
st.write("pandas import 시작 전")

import pandas as pd

st.write("pandas import 성공")

df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

st.write("DataFrame 생성 성공")
st.write(f"평균: {df['a'].mean()}")

dates = pd.date_range("2026-01-01", periods=5)
st.write(f"date_range 생성 성공: {dates}")
