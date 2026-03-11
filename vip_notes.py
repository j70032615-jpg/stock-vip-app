import streamlit as st

# 1. 頁面基礎設定
st.set_page_config(page_title="股票心法 VIP 專屬系統", page_icon="📈", layout="wide")

# 2. 初始化登入狀態 (如果還沒登入，預設為 False)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# ---------------- 側邊欄：登入邏輯 ----------------
with st.sidebar:
    st.markdown("## 🔐 VIP 會員登入")
    
    # 如果還沒登入，顯示輸入框
    if not st.session_state['logged_in']:
        user_id = st.text_input("會員帳號", placeholder="請輸入帳號")
        user_pw = st.text_input("會員密碼", type="password", placeholder="請輸入密碼")
        
        if st.button("立即進入系統", use_container_width=True):
            # --- 這裡設定你的 VIP 帳密 ---
            if user_id == "admin" and user_pw == "888888": 
                st.session_state['logged_in'] = True
                st.success("登入成功！")
                st.rerun() # 重新整理頁面以顯示內容
            else:
                st.error("帳號或密碼錯誤，請洽管理員")
    else:
        # 如果已經登入，顯示歡迎訊息與登出按鈕
        st.success("✅ VIP 權限已啟動")
        if st.button("登出系統"):
            st.session_state['logged_in'] = False
            st.rerun()

    st.divider()
    st.info("💡 只有通過驗證的 VIP 成員才能查看下方心法目錄。")

# ---------------- 主頁面：內容控管 ----------------
left_spacer, main_content, right_spacer = st.columns([1, 2, 1])

with main_content:
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📈 股票心法 VIP 系統</h1>", unsafe_allow_html=True)
    st.write("---")

    # 🔑 關鍵控管邏輯
    if st.session_state['logged_in']:
        # --- 只有登入後才會顯示的部分 ---
        st.markdown("<p style='text-align: center; color: green; font-weight: bold;'>歡迎回來，尊貴的 VIP 會員</p>", unsafe_allow_html=True)
        
        menu_items = [
            "一. 畫趨勢線確認位置", "二. 畫箱型 + 波段 + 壓力支撐線", 
            "三. 用箱形突破找加碼點跟出場點", "四. 均線做法", 
            "五. 懶人高勝法", "六. 單純找裸K選股", 
            "七. 資金分配法", "八. 精準支撐壓力", 
            "九. 緊急下跌狀況注意提醒"
        ]
        
        for i, item in enumerate(menu_items):
            if st.button(item, key=f"vip_{i}", use_container_width=True):
                st.subheader(f"📍 進入心法：{item}")
                st.info("內容讀取中...")
                # 這裡以後可以根據不同的 item 顯示不同的心法內容
    
    else:
        # --- 未登入時顯示的畫面 ---
        st.warning("⚠️ 此為 VIP 專屬內容，請先從左側登入。")
        st.image("https://via.placeholder.com/800x400.png?text=Please+Login+to+View+VIP+Content") # 這裡可以放一張漂亮的預覽圖

    st.write("---")
    st.caption("© 2026 股票心法 VIP 系統 | 核心加密技術：比爾蓋茲")
