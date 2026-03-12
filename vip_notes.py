import streamlit as st

# --- 1. 頁面基本配置 ---
st.set_page_config(page_title="股票十大心法 VIP 系統", layout="wide", page_icon="📈")

# --- 2. 核心狀態保持 ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "主目錄"

# --- 3. 側邊欄：登入介面 ---
with st.sidebar:
    st.title("🔐 VIP 會員中心")
    if not st.session_state['logged_in']:
        u = st.text_input("輸入帳號")
        p = st.text_input("輸入密碼", type="password")
        if st.button("確認進入系統", use_container_width=True):
            if u == "1234" and p == "1234":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("❌ 帳密不正確")
    else:
        st.success("✅ VIP 權限已啟動")
        if st.button("安全登出系統", use_container_width=True):
            st.session_state['logged_in'] = False
            st.session_state['tab'] = "主目錄"
            st.rerun()
    st.divider()
    st.caption("核心開發：比爾蓋茲 | 2026 穩定版")

# --- 4. 主畫面內容 ---
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📈 股票心法 VIP 專屬系統</h1>", unsafe_allow_html=True)
st.write("---")

# 檢查登入狀態
if st.session_state['logged_in']:
    
    # 情況 A：在主目錄，顯示九宮格按鈕
    if st.session_state['tab'] == "主目錄":
        st.markdown("<h3 style='text-align: center;'>請選擇研讀心法</h3>", unsafe_allow_html=True)
        
        menu = [
            "一. 畫趨勢線確認位置", "二. 畫箱型 + 波段 + 壓力支撐線", 
            "三. 用箱形突破找加碼點跟出場點", "四. 均線做法", 
            "五. 懶人穩勝法", "六. 單純找裸K選股", 
            "七. 資金分配法", "八. 精準支撐壓力", 
            "九. 緊急下跌狀況注意提醒"
        ]
        
        # 建立 3x3 矩陣按鈕
        cols = st.columns(3)
        for i, item in enumerate(menu):
            with cols[i % 3]:
                # 這裡就是你最愛的藍色大按鈕
                if st.button(item, key=f"btn_{i}", use_container_width=True):
                    st.session_state['tab'] = item
                    st.rerun()
                    
    # 情況 B：進入特定心法內容
    else:
        curr = st.session_state['tab']
        st.subheader(f"📍 當前位置：{curr}")
        
        # --- 各別心法功能區 ---
        if "一." in curr:
            st.write("### 趨勢線戰術：確認多空分界")
            st.info("💡 核心：年線找支撐，20MA 爆量站穩進場。")

        elif "二." in curr or "三." in curr:
            st.write("### 🧮 箱型自動精算工具")
            c1, c2 = st.columns(2)
            with c1: hp = st.number_input("箱型最高價 (壓力)", value=100.0)
            with c2: lp = st.number_input("箱型最低價 (支撐)", value=90.0)
            
            diff = hp - lp
            st.divider()
            m1, m2 = st.columns(2)
            m1.metric("🛡️ 中軸守備線", f"{lp + diff/2:.2f}")
            m2.metric("🚀 第二波目標", f"{hp + diff:.2f}")

        elif "七." in curr:
            st.write("### 💰 資金配置計算")
            total = st.number_input("擬投入總額 (萬元)", value=100.0)
            st.success(f"建議：高股息 {total*0.6:.1f}萬 / 波動型 {total*0.3:.1f}萬 / 短線 {total*0.1:.1f}萬")

        elif "九." in curr:
            st.error("🆘 緊急避險保命清單")
            st.checkbox("1. 5分線站上 200MA？")
            st.checkbox("2. 1小時 60MA 沒跌破？")
            st.checkbox("3. 今日 15分線最大量 K 棒低點守住？")

        # 返回主目錄按鈕
        st.write("---")
        if st.button("⬅️ 返回九宮格目錄"):
            st.session_state['tab'] = "主目錄"
            st.rerun()

else:
    # 未登入提示
    st.warning("🔒 本系統為 VIP 專屬內容，請先由側邊欄登入。")
    st.info("💡 預設帳號：1234 / 密碼：1234")

st.write("---")
st.caption("© 2026 股票心法 VIP | 資料來源：用戶提供之核心戰術")
