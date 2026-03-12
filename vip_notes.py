import streamlit as st

# 1. 頁面基本配置
st.set_page_config(page_title="股票心法 VIP 系統", layout="wide", page_icon="📈")

# 2. 核心狀態保持 (防止按鈕點了沒反應)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "主目錄"

# --- 側邊欄設計 ---
with st.sidebar:
    st.title("🔐 會員中心")
    if not st.session_state['logged_in']:
        u = st.text_input("帳號")
        p = st.text_input("密碼", type="password")
        if st.button("點我登入", use_container_width=True):
            if u == "1234" and p == "1234":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("帳密錯誤")
    else:
        st.success("✅ VIP 已啟動")
        if st.button("安全登出"):
            st.session_state['logged_in'] = False
            st.session_state['tab'] = "主目錄"
            st.rerun()
    st.divider()
    st.caption("技術支援：比爾蓋茲")

# --- 主畫面內容 ---
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📈 股票心法 VIP 系統</h1>", unsafe_allow_html=True)
st.write("---")

# 判斷是否登入
if st.session_state['logged_in']:
    
    # 如果在主目錄：顯示九個大按鈕 (這就是你原本最喜歡的畫面)
    if st.session_state['tab'] == "主目錄":
        menu = [
            "一. 畫趨勢線確認位置", "二. 畫箱型 + 波段 + 壓力支撐線", 
            "三. 用箱形突破找加碼點跟出場點", "四. 均線做法", 
            "五. 懶人穩勝法", "六. 單純找裸K選股", 
            "七. 資金分配法", "八. 精準支撐壓力", 
            "九. 緊急下跌狀況注意提醒"
        ]
        
        # 建立三欄式矩陣按鈕
        cols = st.columns(3)
        for i, item in enumerate(menu):
            with cols[i % 3]:
                if st.button(item, key=f"main_btn_{i}", use_container_width=True):
                    st.session_state['tab'] = item
                    st.rerun()
                    
    # 如果已經點進去某個心法
    else:
        curr = st.session_state['tab']
        st.subheader(f"📍 當前心法：{curr}")
        
        # 內容顯示區
        if "一." in curr:
            st.write("### 趨勢線筆記")
            st.write("1. 找年線高低點。2. 站上 20MA 爆量進場。")
            # 預留圖片顯示位置
            # st.image("notes_1.jpg")

        elif "二." in curr or "三." in curr:
            # 恢復箱型計算機
            hp = st.number_input("箱型最高 (壓力)", value=100.0)
            lp = st.number_input("箱型最低 (支撐)", value=90.0)
            diff = hp - lp
            st.metric("🛡️ 中軸守備線", f"{lp + diff/2:.2f}")
            st.metric("🚀 第二波目標", f"{hp + diff:.2f}")

        elif "七." in curr:
            # 恢復資產分配
            total = st.number_input("總資產 (萬元)", value=100.0)
            st.info(f"建議：高股息 {total*0.6:.1f} 萬 / 波動型 {total*0.3:.1f} 萬")

        elif "九." in curr:
            # 恢復保命清單
            st.error("⚠️ 緊急保命檢查")
            st.checkbox("1. 5分線站上 200MA？")
            st.checkbox("2. 1小時 60MA 沒破？")

        # 返回按鈕
        if st.button("⬅️ 返回九宮格目錄"):
            st.session_state['tab'] = "主目錄"
            st.rerun()

else:
    # 沒登入時顯示的提示
    st.warning("🔒 本內容僅限 VIP 會員。請從側邊欄輸入帳密登入。")
    st.info("💡 預設測試帳密為：1234 / 1234")

st.write("---")
st.caption("© 2026 股票心法 VIP")
