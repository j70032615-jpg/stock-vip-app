import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

# 1. 頁面配置
st.set_page_config(page_title="股票心法 VIP 3.1", layout="wide", page_icon="🚀")

# 2. 初始化狀態
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "自動化診斷"

# --- 側邊欄 ---
with st.sidebar:
    st.title("🔐 會員系統")
    if not st.session_state['logged_in']:
        u = st.text_input("帳號", key="u")
        p = st.text_input("密碼", type="password", key="p")
        if st.button("確認進入系統"):
            if u == "1234" and p == "1234":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("密碼錯誤")
    else:
        st.success("✅ VIP 已登入")
        if st.button("📈 自動化診斷"): st.session_state['tab'] = "自動化診斷"
        if st.button("📖 九大心法筆記"): st.session_state['tab'] = "心法筆記"
        if st.button("登出"):
            st.session_state['logged_in'] = False
            st.rerun()

# --- 主畫面 ---
if not st.session_state['logged_in']:
    st.info("💡 請在左側輸入帳號密碼 1234")
else:
    if st.session_state['tab'] == "自動化診斷":
        st.header("🚀 股票自動化診斷")
        symbol = st.text_input("輸入代碼 (台股加 .TW)", "2330.TW")
        if st.button("開始診斷"):
            df = yf.download(symbol, period="5y")
            if not df.empty:
                df['MA20'] = df['Close'].rolling(window=20).mean()
                df['MA60'] = df['Close'].rolling(window=60).mean()
                st.metric("當前股價", f"${round(float(df['Close'].iloc[-1]), 2)}")
                st.line_chart(df[['Close', 'MA20', 'MA60']])
                st.success("診斷完成！MA20 為生命線，跌破請注意風險。")
            else:
                st.error("代碼錯誤，請檢查格式。")

    elif st.session_state['tab'] == "心法筆記":
        st.header("📖 股票九大心法 (VIP 版)")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 1-4 心法\n- **趨勢**：均線沒抬頭不買。\n- **選股**：汰弱留強。\n- **量能**：無量不漲。\n- **停損**：10% 鐵律。")
        with col2:
            st.markdown("### 5-9 心法\n- **心態**：戒貪戒躁。\n- **均線**：20MA 生命線。\n- **資金**：分批配置。\n- **週期**：看大做小。\n- **覆盤**：每日檢討。")
