import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

# 1. 頁面基礎配置
st.set_page_config(page_title="股票心法 VIP 3.0", layout="wide", page_icon="🚀")

# 2. 初始化 Session 狀態
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "自動化診斷"

# --- 側邊欄：VIP 登入驗證 ---
with st.sidebar:
    st.title("🔐 會員系統")
    if not st.session_state['logged_in']:
        u = st.text_input("帳號", key="user_input")
        p = st.text_input("密碼", type="password", key="pass_input")
        if st.button("確認進入系統", use_container_width=True):
            if u == "1234" and p == "1234":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("密碼錯誤")
    else:
        st.success("✅ VIP 會員已登入")
        if st.button("登出系統"):
            st.session_state['logged_in'] = False
            st.rerun()
        
        st.divider()
        st.subheader("功能選單")
        if st.button("📈 自動化診斷與回測", use_container_width=True):
            st.session_state['tab'] = "自動化診斷"
        if st.button("📖 完整九大心法筆記", use_container_width=True):
            st.session_state['tab'] = "心法筆記"

# --- 主畫面內容 ---
if not st.session_state['logged_in']:
    st.info("💡 請在左側輸入帳號密碼 1234 以解鎖 VIP 功能。")
else:
    if st.session_state['tab'] == "自動化診斷":
        st.header("🚀 股票自動化診斷與十年回測")
        symbol = st.text_input("請輸入股票代碼 (台股請加 .TW，例如: 2330.TW)", "AAPL")
        
        if st.button("開始診斷"):
            with st.spinner('大數據計算中...'):
                df = yf.download(symbol, period="10y")
                if not df.empty:
                    # 技術指標計算
                    df['MA20'] = df['Close'].rolling(window=20).mean()
                    df['MA60'] = df['Close'].rolling(window=60).mean()
                    
                    # 回測邏輯
                    df['Signal'] = 0
                    df.loc[df['MA20']
