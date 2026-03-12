import streamlit as st

# 1. 頁面配置
st.set_page_config(page_title="股票心法 VIP 系統", layout="wide", page_icon="📈")

# 2. 狀態初始化
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "主目錄"

# --- 側邊欄：登入 ---
with st.sidebar:
    st.title("🔐 會員登入")
    if not st.session_state['logged_in']:
        u = st.text_input("帳號")
        p = st.text_input("密碼", type="password")
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
# 登入後才顯示大按鈕
if st.session_state['logged_in']:
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📈 股票心法 VIP 核心系統</h1>", unsafe_allow_html=True)
    st.write("---")

    # 如果在主目錄，顯示九大按鈕
    if st.session_state['tab'] == "主目錄":
        menu = [
            "一. 畫趨勢線確認位置", "二. 畫箱型 + 波段 + 壓力支撐線", 
            "三. 用箱形突破找加碼點跟出場點", "四. 均線做法", 
            "五. 懶人穩勝法", "六. 單純找裸K選股", 
            "七. 資金分配法", "八. 精準支撐壓力", 
            "九. 緊急下跌狀況注意提醒"
        ]
        
        # 3列排列，更有 APP 的質感
        cols = st.columns(3)
        for i, item in enumerate(menu):
            with cols[i % 3]:
                if st.button(item, key=f"menu_{i}", use_container_width=True):
                    st.session_state['tab'] = item
    
    # 如果點進去心法了
    else:
        curr = st.session_state['tab']
        st.subheader(f"📍 當前心法：{curr}")
        
        if "一." in curr:
            st.write("### 趨勢線筆記")
            st.write("1. 找年線高低點。2. 站上 20MA 爆量進場。")
            # 這裡就是你可以放圖片的地方
            # st.image("notes_1.jpg")

        elif "二." in curr or "三." in curr:
            # 恢復你最愛的計算機
            hp = st.number_input("箱型最高", value=100.0)
            lp = st.number_input("箱型最低", value=90.0)
            diff = hp - lp
            st.metric("🛡️ 中軸守備線", f"{lp + diff/2:.2f}")
            st.metric("🚀 第二波目標", f"{hp + diff:.2f}")

        elif "七." in curr:
            total = st.number_input("總資產 (萬元)", value=100.0)
            st.info(f"建議：高股息 {total*0.6:.0f}萬 / 波動型 {total*0.3:.0f}萬")

        elif "九." in curr:
            st.error("⚠️ 緊急保命清單")
            st.checkbox("1. 5分線站上 200MA？")
            st.checkbox("2. 1小時線 60MA 沒破？")

        if st.button("⬅️ 返回心法目錄"):
            st.session_state['tab'] = "主目錄"
            st.rerun()
else:
    st.warning("🔒 請先於左側登入帳號密碼 (1234)。")

st.write("---")
st.caption("© 2026 股票心法 VIP")
