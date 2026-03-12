import streamlit as st

# 1. 頁面配置
st.set_page_config(page_title="股票十大心法 VIP 系統", layout="wide", page_icon="📈")

# 2. 安全帳密清單 (這裡就是你的新保險箱，不用再開試算表了！)
VIP_USERS = {
    "1234": "1234",       # 你的主帳號
    "bill": "win888",     # 你可以隨意增加帳號：密碼
    "guest": "9999"       # 給朋友試用的帳號
}

# 3. 初始化狀態
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "主目錄"

# --- 側邊欄：登入介面 ---
with st.sidebar:
    st.title("🔐 VIP 會員中心")
    if not st.session_state['logged_in']:
        u_input = st.text_input("VIP 帳號")
        p_input = st.text_input("登入密碼", type="password")
        if st.button("確認進入系統", use_container_width=True):
            # 檢查輸入的帳密是否在清單中
            if u_input in VIP_USERS and VIP_USERS[u_input] == p_input:
                st.session_state['logged_in'] = True
                st.success(f"歡迎回來，{u_input}！")
                st.rerun()
            else:
                st.error("❌ 帳號或密碼不對喔！")
    else:
        st.success(f"✅ VIP：{st.session_state.get('user', '權限已啟動')}")
        if st.button("🚪 安全登出系統", use_container_width=True):
            st.session_state['logged_in'] = False
            st.session_state['tab'] = "主目錄"
            st.rerun()
    st.divider()
    st.caption("核心技術：比爾蓋茲安全防護")

# --- 主畫面佈局 ---
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📈 股票十大心法 VIP 系統</h1>", unsafe_allow_html=True)
st.write("---")

if st.session_state['logged_in']:
    # 登入成功後看到的九宮格
    if st.session_state['tab'] == "主目錄":
        menu = [
            "一. 畫趨勢線確認位置", "二. 畫箱型 + 波段 + 壓力支撐線", 
            "三. 用箱形突破找加碼點跟出場點", "四. 均線做法", 
            "五. 懶人穩勝法", "六. 單純找裸K選股", 
            "七. 資金分配法", "八. 精準支撐壓力", 
            "九. 緊急下跌狀況注意提醒"
        ]
        
        cols = st.columns(3)
        for i, item in enumerate(menu):
            with cols[i % 3]:
                if st.button(item, key=f"btn_{i}", use_container_width=True):
                    st.session_state['tab'] = item
                    st.rerun()
    else:
        # 心法內容頁
        curr = st.session_state['tab']
        st.subheader(f"📍 當前心法：{curr}")
        
        # 範例功能：心法二/三的計算機
        if "二." in curr or "三." in curr:
            h = st.number_input("箱型最高", value=100.0)
            l = st.number_input("箱型最低", value=90.0)
            st.metric("中軸守備位", f"{(h+l)/2:.2f}")

        # 返回按鈕
        if st.button("⬅️ 返回心法目錄"):
            st.session_state['tab'] = "主目錄"
            st.rerun()
else:
    st.warning("🔒 內容已加密，請從側邊欄登入 VIP 帳號以解鎖心法按鈕。")

st.write("---")
