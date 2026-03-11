import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

# 1. 頁面基礎配置
st.set_page_config(page_title="股票心法 VIP 2.0", layout="wide", page_icon="📈")

# 2. 初始化 Session 狀態
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "主目錄"

# --- 側邊欄：VIP 登入驗證 ---
with st.sidebar:
    st.title("🔐 會員登入")
    if not st.session_state['logged_in']:
        u = st.text_input("帳號", key="user_input")
        p = st.text_input("密碼", type="password", key="pass_input")
        if st.button("確認進入系統", use_container_width=True):
            if u == "1234" and p == "1234":
                st.session_state['logged_in'] = True
                st.success("驗證成功！歡迎 VIP 使用")
                st.rerun()
            else:
                st.error("密碼錯誤，請洽管理員")
    else:
        st.write("✅ 已登入 VIP 模式")
        if st.button("登出系統"):
            st.session_state['logged_in'] = False
            st.rerun()
        
        st.divider()
        st.write("### 功能導覽")
        if st.button("🚀 自動化診斷與回測", use_container_width=True):
            st.session_state['tab'] = "自動化診斷"
        if st.button("📖 股票心法筆記", use_container_width=True):
            st.session_state['tab'] = "心法筆記"

# --- 主畫面內容 ---
if not st.session_state['logged_in']:
    st.info("請於左側輸入 VIP 帳號密碼以開啟功能。")
else:
    if st.session_state['tab'] == "自動化診斷":
        st.header("🚀 股票自動化診斷與十年回測")
        symbol = st.text_input("請輸入股票代碼 (例如: AAPL 或 2330.TW)", "AAPL")
        
        if st.button("開始診斷"):
            with st.spinner('正在從 Yahoo Finance 抓取大數據...'):
                # 抓取資料
                df = yf.download(symbol, period="10y")
                if not df.empty:
                    # 計算技術指標 (純手工計算，不依賴外部套件)
                    df['MA20'] = df['Close'].rolling(window=20).mean()
                    df['MA60'] = df['Close'].rolling(window=60).mean()
                    
                    # 簡單回測邏輯 (20MA > 60MA 黃金交叉)
                    df['Signal'] = 0
                    df.loc[df['MA20'] > df['MA60'], 'Signal'] = 1
                    df['Returns'] = df['Close'].pct_change()
                    df['Strategy_Returns'] = df['Signal'].shift(1) * df['Returns']
                    
                    cum_returns = (1 + df['Strategy_Returns'].fillna(0)).cumprod()
                    
                    # 顯示數據指標
                    col1, col2, col3 = st.columns(3)
                    final_ret = round((cum_returns.iloc[-1]-1)*100, 2)
                    col1.metric("十年累計報酬率", f"{final_ret}%")
                    col2.metric("目前價格", f"${round(df['Close'].iloc[-1], 2)}")
                    col3.metric("趨勢狀態", "多頭" if df['MA20'].iloc[-1] > df['MA60'].iloc[-1] else "空頭")
                    
                    st.write("### 📈 十年資產成長曲線")
                    st.line_chart(cum_returns)
                    
                    st.write("### 📊 近期歷史數據預覽")
                    st.dataframe(df.tail(10))
                else:
                    st.error("找不到該股票代碼，請檢查格式是否正確。")

    elif st.session_state['tab'] == "心法筆記":
        st.header("📖 股票心法 VIP 專屬筆記")
        st.write("""
        ### 1. 均線戰法 (由 AI 自動判斷)
        - **黃金交叉**：20MA 上穿 60MA，代表中長期趨勢轉強，適合做多。
        - **死亡交叉**：20MA 下穿 60MA，代表趨勢轉弱，應考慮減碼。
        
        ### 2. VIP 紀律提醒
        - 永遠不要在情緒激動時加碼。
        - 停損必須堅決執行（建議設在 -10%）。
        - 觀察累計報酬曲線，如果曲線向下，代表目前的策略不適合該股票。
        """)
