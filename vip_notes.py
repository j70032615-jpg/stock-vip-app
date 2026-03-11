import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

# 1. 頁面配置
st.set_page_config(page_title="股票心法 VIP 3.2", layout="wide", page_icon="🚀")

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
        if st.button("確認進入系統", use_container_width=True):
            if u == "1234" and p == "1234":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("密碼錯誤")
    else:
        st.success("✅ VIP 已登入")
        if st.button("📈 自動化診斷", use_container_width=True): st.session_state['tab'] = "自動化診斷"
        if st.button("📖 完整九大心法", use_container_width=True): st.session_state['tab'] = "心法筆記"
        st.divider()
        if st.button("安全登出", use_container_width=True):
            st.session_state['logged_in'] = False
            st.rerun()

# --- 主畫面 ---
if not st.session_state['logged_in']:
    st.info("🔒 歡迎來到 VIP 專屬系統，請由左側登入。")
else:
    if st.session_state['tab'] == "自動化診斷":
        st.header("🚀 股票自動化診斷與五年回測")
        symbol = st.text_input("請輸入股票代碼 (台股範例: 2330.TW)", "2330.TW")
        if st.button("開始執行大數據診斷"):
            with st.spinner('計算中...'):
                df = yf.download(symbol, period="5y")
                if not df.empty:
                    df['MA20'] = df['Close'].rolling(window=20).mean()
                    df['MA60'] = df['Close'].rolling(window=60).mean()
                    
                    col1, col2, col3 = st.columns(3)
                    col1.metric("當前股價", f"${round(float(df['Close'].iloc[-1]), 2)}")
                    status = "🔥 多頭排列" if df['MA20'].iloc[-1] > df['MA60'].iloc[-1] else "❄️ 空頭排列"
                    col2.metric("趨勢診斷", status)
                    col3.metric("20MA 位置", f"${round(float(df['MA20'].iloc[-1]), 2)}")
                    
                    st.line_chart(df[['Close', 'MA20', 'MA60']])
                    st.success(f"✅ {symbol} 診斷完成。記住：20MA 是你的生命線！")
                else:
                    st.error("找不到股票數據，台股請記得加 .TW")

    elif st.session_state['tab'] == "心法筆記":
        st.header("📖 股票九大心法 (VIP 完整精華版)")
        st.markdown("---")
        
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("一、趨勢心法")
            st.write("👉 **不預測底部**：均線沒抬頭，絕對不買。多頭做多，空頭持幣順勢而為。")
            
            st.subheader("二、選股心法")
            st.write("👉 **汰弱留強**：只買強勢股，不攤平弱勢股。同族群只選最強的指標龍頭。")
            
            st.subheader("三、量能心法")
            st.write("👉 **無量不漲**：量縮是整理，補量才是發動。高檔爆量需警惕主力出貨。")
            
            st.subheader("四、停損心法")
            st.write("👉 **10% 鐵律**：損失達 10% 必須無條件離場，不帶任何感情回頭。")

            st.subheader("五、心態心法")
            st.write("👉 **戒貪戒躁**：買點是等出來的，不是追出來的。保持心如止水。")

        with c2:
            st.subheader("六、均線心法")
            st.write("👉 **20MA 生命線**：回測支撐買進，一旦有效跌破，果斷撤退不留戀。")
            
            st.subheader("七、資金心法")
            st.write("👉 **分批配置**：雞蛋不放同一個籃子。分批進場給自己留有容錯空間。")
            
            st.subheader("八、週期心法")
            st.write("👉 **看大做小**：週線看趨勢定方向，日線找精確買賣點。")
            
            st.subheader("九、覆盤心法")
            st.write("👉 **每日檢討**：賺錢要知原因，虧錢要找教訓。持續進化才是贏家。")
            
        st.divider()
        st.info("💡 這是我們共同調校出的操盤邏輯，請務必內化。")
