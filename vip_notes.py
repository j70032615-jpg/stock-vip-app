import streamlit as st
import pandas as pd

# 1. 基礎連線設定
SHEET_ID = "1oWgZi4LPnYfwe22sG2MJOzZCj1LkUXysQ-pAG-3Pr98"
SHEET_NAME = "VIP名單" 
URL_USERS = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

st.set_page_config(page_title="股票十大心法 VIP 系統", layout="wide")

# 初始化登入狀態
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- 登入畫面 ---
if not st.session_state.logged_in:
    st.title("🔐 股票十大心法 VIP 系統")
    st.warning("本系統僅限 VIP 會員使用，請輸入帳號密碼解鎖內容。")
    
    with st.form("login_form"):
        u = st.text_input("VIP 帳號")
        p = st.text_input("登入密碼", type="password")
        if st.form_submit_button("登入系統"):
            try:
                df = pd.read_csv(URL_USERS)
                match = False
                for i, r in df.iterrows():
                    # 抓 A 欄帳號與 B 欄密碼
                    if str(u).strip() == str(r[0]).strip() and str(p).strip() == str(r[1]).strip():
                        match = True
                        break
                if match:
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("❌ 帳密錯誤，請確認試算表 A2, B2 資料")
            except:
                st.error("⚠️ 連線失敗，請檢查試算表是否已『發布到網路』")

# --- VIP 核心心法區 (登入成功後才會看到) ---
else:
    # 側邊欄設定
    st.sidebar.success("✅ VIP 權限已啟用")
    if st.sidebar.button("登出系統"):
        st.session_state.logged_in = False
        st.rerun()
    
    st.title("📈 股票十大心法 - 核心戰術庫")
    
    # 建立目錄分頁
    tabs = st.tabs(["1-3 趨勢與箱型", "4-6 進出場訊號", "7-10 資金與風險", "緊急避險指南"])

    with tabs[0]:
        st.header("一、畫趨勢線與箱型心法")
        st.markdown("""
        * **趨勢大方向**：建議用年線畫趨勢線，找大波段低點。
        * **爆量下影線**：找爆量棒位置，這通常是止跌或轉折訊號。
        * **箱型突破**：
            1. 從爆量低點畫到前波高點為一波。
            2. 畫出正方形箱型。
            3. 箱型突破且 K 棒站上 20MA 為新波段開始。
        """)

    with tabs[1]:
        st.header("二、進場、加碼與出場策略")
        st.markdown("""
        * **最強進場點**：K 棒在 20MA 爆量上漲。
        * **加碼時機**：跌回箱型起漲點但不跌破，或 1/5 分線站上 200MA。
        * **短線出場**：K 棒爆量跌破 5MA 立即先走。
        * **波段出場**：1 小時線跌破 60MA 或周線跌破 20MA。
        """)

    with tabs[2]:
        st.header("三、資金分配與心理建設")
        st.markdown("""
        * **60% 資金**：長抱 2 檔高股息 ETF (00919, 0056)。
        * **30% 資金**：挑 1 檔波動型 ETF。
        * **10% 資金**：短線個股或當急用金。
        * **心法守則**：獲利 20% 出場部分資金，跌 20% 則分批回補。
        * **增強心理**：看 4 小時 K 線減少盯盤波動，不盯數字只盯 K 棒。
        """)

    with tabs[3]:
        st.header("🆘 緊急下跌狀況必讀")
        st.error("大跌發生時，請冷靜檢查以下事項：")
        st.markdown("""
        1. **看均線**：1 小時線 60MA 是否跌破？跌破先出場！
        2. **看量能**：早盤 15 分線最大量 K 棒是否被跌破？
        3. **看期貨**：注意是否為期貨結算日，機率性持續下跌。
        4. **假突破**：發現假突破進場可馬上出場，轉真突破再追回。
        """)
