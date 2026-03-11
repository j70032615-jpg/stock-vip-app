import streamlit as st
import pandas as pd

# 1. 設定你的 Google 試算表發布網址 (CSV 格式)
SHEET_ID = "1oWgZi4LPnYfwe22sG2MJOzZCj1LkUXysQ-pAG-3Pr98"
URL_USERS = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid=1834495482"

st.set_page_config(page_title="股票心法 VIP 筆記本", layout="wide")

# 初始化登入狀態
if "vip_auth" not in st.session_state:
    st.session_state.vip_auth = False

# --- 登入畫面 ---
if not st.session_state.vip_auth:
    st.title("📈 股票心法 VIP 專屬系統")
    st.subheader("請登入以查看專業筆記圖片")
    
    with st.container(border=True):
        user = st.text_input("會員帳號")
        pw = st.text_input("會員密碼", type="password")
        
        if st.button("立即進入系統", use_container_width=True):
            try:
                # 讀取資料並清除所有空白
                df = pd.read_csv(URL_USERS).astype(str)
                df.columns = [c.strip() for c in df.columns]
                
                # 專業比對邏輯：只要有一組帳密對上就過
                match = False
                for _, row in df.iterrows():
                    if user.strip() == row[0].strip() and pw.strip() == row[1].strip():
                        match = True
                        break
                
                if match:
                    st.session_state.vip_auth = True
                    st.rerun()
                else:
                    st.error("❌ 帳號或密碼錯誤，請聯繫管理員")
            except:
                st.error("⚠️ 讀取名單失敗！請檢查試算表是否已『發布到網路』")

# --- VIP 內容區 ---
else:
    st.sidebar.title("VIP 導航選單")
    page = st.sidebar.radio("心法分類", ["📊 核心趨勢筆記", "🕯️ K線型態圖解", "💰 資金分配策略"])
    
    if st.sidebar.button("登出系統"):
        st.session_state.vip_auth = False
        st.rerun()

    st.title(f"【{page}】")

    if page == "📊 核心趨勢筆記":
        st.info("這是我親手畫的趨勢線重點，請仔細研讀：")
        # 這裡放入你的筆記圖片網址
        # st.image("你的圖片網址.jpg", caption="心法一：畫線技巧")
        st.markdown("""
        ### 今日重點：
        - 畫出爆量 K 棒低點。
        - 觀察 20MA 是否有支撐。
        """)
        
    elif page == "🕯️ K線型態圖解":
        st.warning("VIP 限定：爆量下影線的秘密")
        # 示範顯示圖片的功能
        # st.image("你的另一張筆記.jpg")

    st.success("✅ 更多心法圖片將定期更新於此。")
