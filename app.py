import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="SK하이닉스 주가 대시보드", layout="wide")

st.title("📈 SK하이닉스 주가 대시보드")

# SK하이닉스 종목 코드: 000660.KS (코스피)
TICKER = "000660.KS"

# 사이드바에서 기간 선택
period = st.sidebar.selectbox(
    "조회 기간",
    ["1mo", "3mo", "6mo", "1y", "2y"],
    index=2,
)

@st.cache_data(ttl=3600)
def load_data(ticker, period):
    df = yf.Ticker(ticker).history(period=period)
    return df

df = load_data(TICKER, period)

if df.empty:
    st.error("데이터를 가져오지 못했습니다.")
else:
    # 최신 종가 표시
    latest = df["Close"].iloc[-1]
    prev = df["Close"].iloc[-2]
    change = latest - prev
    change_pct = (change / prev) * 100

    col1, col2 = st.columns(2)
    col1.metric("현재가", f"{latest:,.0f}원", f"{change:,.0f}원 ({change_pct:+.2f}%)")

    # 캔들스틱 차트
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
    )])
    fig.update_layout(title="주가 차트", xaxis_title="날짜", yaxis_title="가격(원)")
    st.plotly_chart(fig, use_container_width=True)

    # 원본 데이터 표
    st.subheader("데이터 테이블")
    st.dataframe(df.tail(20))
