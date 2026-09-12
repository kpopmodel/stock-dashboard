import streamlit as st

st.title("테스트 5: numpy만 단독 테스트")
st.write("numpy import 시작 전")

import numpy as np

st.write("numpy import 성공")

arr = np.random.randint(1700, 1900, 30)

st.write(f"numpy 연산 성공: 평균 = {arr.mean()}")
