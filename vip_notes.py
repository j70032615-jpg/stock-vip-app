import streamlit as st
import pandas as pd

# 1. 基礎設定：這是您的試算表分身，絕對不能少
SHEET_ID = "1oWgZi4LPnYfwe22sG2MJOzZCj1LkUXysQ-pAG-3Pr98"
SHEET_NAME = "VIP名單" 

# 2. 定位分頁：一個抓心法，一個抓VIP名單
URL_USERS = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

st.set_page_config(page_title="股票十大心法 VIP 系統", layout="wide")

# 初始化登入狀態
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- 登入系統介面 ---
if not st.session_state.logged_in:
    st.title("🔐 股票十大心法 VIP 系統")
    st.info("請輸入您的 VIP 帳號密碼。")
    
    with st.form("login_form"):
        u = st.text_input("帳號")
        p = st.text_input("密碼", type="password")
        if st.form_submit_button("登入"):
            try:
                df = pd.read_csv(URL_USERS)
                # 逐行比對資料
                match = False
                for i, r in df.iterrows():
                    if str(u).strip() == str(r[0]).strip() and str(p).strip() == str(r[1]).strip():
                        match = True
                        break
                if match:
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("帳號密碼有誤")
            except:
                st.error("連線失敗，請檢查試算表發布狀態")

# --- 核心心法展示區 ---
else:
    st.sidebar.success("✅ VIP 已登入")
    if st.sidebar.button("登出"):
        st.session_state.logged_in = False
        st.rerun()

    st.title("📈 股票十大心法內容")
    
    t1, t2, t3 = st.tabs(["核心心法", "緊急狀況", "資金分配"])

    with t1:
        st.header("一. 畫趨勢線心法")
        st.write("1. 畫趨勢線：建議用年線畫，找大方向。")
        st.write("2. 爆量位置：注意爆量下影線。")
        st.write("3. 進場：K棒在 20MA 爆量上漲進場。")

    with t2:
        st.header("二. 緊急下跌提醒")
        st.warning("⚠️ 檢查清單：")
        st.write("1. 結算日風險：期貨結算日機率性下跌。")
        st.write("2. 1小時線：60MA 跌破先出場。")

    with t3:
        st.header("三. 資金分配")
        st.write("* 60% 資金：挑選 2 檔高股息 ETF (00919, 0056)。")
        st.write("* 30% 資金：1 檔波動型 ETF。")
        st.write("* 10% 資金：短線預備金。")
