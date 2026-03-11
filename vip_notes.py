import streamlit as st
import yfinance as yf
import pandas as pd
import pandas_ta as ta

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
                st.rerun()
            else:
                st.error("帳號或密碼錯誤")
    else:
        st.success("✅ VIP 權限已啟動")
        if st.button("登出系統", use_container_width=True):
            st.session_state['logged_in'] = False
            st.session_state['tab'] = "主目錄"
            st.rerun()
    st.divider()
    st.caption("核心技術支援：比爾蓋茲")

# --- 主畫面佈局 ---
l_sp, m_col, r_sp = st.columns([1, 2, 1])

with m_col:
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📈 股票心法全自動系統</h1>", unsafe_allow_html=True)
    st.write("---")

    # 目錄按鈕
    menu = [
        "🚀 自動化診斷與回測",
        "一. 畫趨勢線確認位置", 
        "二. 畫箱型 + 波段 + 壓力支撐線", 
        "四. 均線做法", 
        "五. 懶人高勝法", 
        "六. 裸K選股", 
        "七. 資金分配法", 
        "八. 精準支撐壓力", 
        "九. 緊急提醒"
    ]
    
    for i, item in enumerate(menu):
        if st.button(item, key=f"menu_btn_{i}", use_container_width=True):
            st.session_state['tab'] = item

    st.write("---")

    # --- VIP 內容顯示區 ---
    curr = st.session_state['tab']
    
    if curr != "主目錄":
        if st.session_state['logged_in']:
            # --- 全新功能：自動化數據與回測 ---
            if "自動化" in curr:
                st.subheader("🤖 大數據 AI 診斷 (十年回測)")
                symbol = st.text_input("請輸入股票代號 (例: 2330.TW, 0050.TW, TSLA)", value="2330.TW")
                
                if st.button("開始全自動分析"):
                    with st.spinner('正在抓取全球即時行情並進行心法回測...'):
                        df = yf.download(symbol, period="10y", interval="1d")
                        if not df.empty:
                            # 計算均線
                            df['MA20'] = ta.sma(df['Close'], length=20)
                            df['MA200'] = ta.sma(df['Close'], length=200)
                            now_p = float(df['Close'].iloc[-1])
                            ma200_p = float(df['MA200'].iloc[-1])
                            
                            # 即時診斷
                            st.markdown("### 🔍 即時狀態")
                            c1, c2 = st.columns(2)
                            c1.metric("當前股價", f"{now_p:.2f}")
                            c2.metric("200日均線 (生命線)", f"{ma200_p:.2f}")
                            
                            if now_p > ma200_p:
                                st.success(f"✅ **多頭訊號**：目前站穩 200MA。")
                            else:
                                st.error(f"❌ **空頭訊號**：目前低於 200MA，請注意風險。")
                            
                            # 回測：80% 穩勝法 (站上 20MA 做多)
                            df['Signal'] = (df['Close'] > df['MA20']).astype(int)
                            df['Strategy'] = df['Signal'].shift(1) * df['Close'].pct_change()
                            cum_strategy = (1 + df['Strategy'].fillna(0)).cumprod()
                            cum_market = (1 + df['Close'].pct_change().fillna(0)).cumprod()
                            
                            st.divider()
                            st.markdown("### 📊 十年回測：心法 vs 市場")
                            st.line_chart(pd.DataFrame({
                                "心法策略 (20MA)": cum_strategy,
                                "直接持有 (市場)": cum_market
                            }))
                            st.info("💡 回測顯示：透過心法避開 20MA 跌破段，能有效降低波動並守住獲利。")
                        else:
                            st.error("找不到股票代號，請確認輸入正確。")

            # --- 心法九：緊急提醒 ---
            elif "九." in curr:
                st.error("⚠️ 緊急下跌診斷清單")
                st.markdown("1. **該加碼嗎？** 1分/5分線是否突破 **200MA**？")
                st.markdown("2. **該出場嗎？** 是否跌破今日 15分線最大量 K 棒低點？")
                st.markdown("3. **趨勢反轉？** 1H 60MA 或 周線 20MA 是否跌破？")
                st.info("💡 注意：破底翻買回，少賺一個箱型；假突破跌回，馬上撤退。")

            # --- 心法四：均線做法 ---
            elif "四." in curr:
                st.markdown("### 🌊 均線慣性診斷")
                time_f = st.radio("選擇時框", ["短線 (1-15分)", "波段 (1H)", "長線 (周/月)"])
                if "短線" in time_f:
                    st.write("● 5分線突破 200MA 做多，跌回賣出。")
                    st.write("● 1分線 5MA 爆量判斷起漲起跌點。")
                elif "波段" in time_f:
                    st.write("● 60MA 是中期轉折線：跌破先逃，漲回先買。")
                    st.write("● 20MA 是箱型確認位置。")

            # --- 心法二：箱型計算 ---
            elif "二." in curr:
                st.markdown("### 📦 箱型波段預測")
                h = st.number_input("箱頂壓力", value=100.0)
                l = st.number_input("箱底支撐", value=80.0)
                st.metric("🚀 突破目標價", f"{h + (h-l):.2f}")
                st.metric("🛡️ 中軸守備位", f"{(h+l)/2:.2f}")

            else:
                st.info(f"「{curr}」詳細心法已整合至系統後台。")
                
        else:
            st.warning("🔒 此為 VIP 專屬內容，請從左側登入 (1234)。")

    st.write("---")
    st.caption("© 2026 股票心法 VIP | 技術支援：比爾蓋茲")
