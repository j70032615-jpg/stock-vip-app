import streamlit as st

# 1. 頁面基礎配置
st.set_page_config(page_title="股票心法 VIP 系統", layout="wide", page_icon="📈")

# 2. 初始化狀態 (Session State)
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
            # 已依據您的需求修改為 1234 / 1234
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
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📈 股票心法 VIP 系統</h1>", unsafe_allow_html=True)
    st.write("---")

    # 目錄按鈕
    menu = ["一. 趨勢線與盤整切換", "二. 畫箱型波段預測", "七. 資金分配法", "九. 緊急提醒"]
    
    # 這裡顯示簡易目錄，所有人可見
    for i, item in enumerate(menu):
        if st.button(item, key=f"menu_btn_{i}", use_container_width=True):
            st.session_state['tab'] = item

    st.write("---")

    # --- VIP 內容顯示區 (邏輯判斷) ---
    curr = st.session_state['tab']
    
    if curr != "主目錄":
        if st.session_state['logged_in']:
