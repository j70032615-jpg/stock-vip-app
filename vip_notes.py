import streamlit as st

# --- 1. 初始化與配置 ---
st.set_page_config(page_title="股票十大心法 VIP 系統", layout="wide", page_icon="📈")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "主目錄"

# --- 2. 側邊欄：登入系統 ---
with st.sidebar:
    st.title("🔐 會員中心")
    if not st.session_state['logged_in']:
        u = st.text_input("帳號")
        p = st.text_input("密碼", type="password")
        if st.button("確認進入系統", use_container_width=True):
            # 目前採安全硬編碼，保護你的 CSV 不外洩
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
    st.caption("技術支援：比爾蓋茲 | 2026 版")

# --- 3. 主畫面邏輯 ---
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📈 股票十大心法 VIP 系統</h1>", unsafe_allow_html=True)
st.write("---")

if not st.session_state['logged_in']:
    st.info("💡 歡迎使用！本系統內含核心戰術、自動精算工具。請由左側登入以開啟完整功能。")
else:
    # 建立九大目錄按鈕
    menu = [
        "一. 畫趨勢線確認位置", "二. 畫箱型 + 波段 + 壓力支撐線", 
        "三. 用箱形突破找加碼點跟出場點", "四. 均線做法", 
        "五. 懶人穩勝法", "六. 單純找裸K選股", 
        "七. 資金分配法", "八. 精準支撐壓力", 
        "九. 緊急下跌狀況注意提醒"
    ]
    
    # 目錄按鈕顯示 (3x3 矩陣)
    cols = st.columns(3)
    for i, item in enumerate(menu):
        with cols[i % 3]:
            if st.button(item, key=f"menu_{i}", use_container_width=True):
                st.session_state['tab'] = item

    st.write("---")
    curr = st.session_state['tab']

    if curr == "主目錄":
        st.write("### 👈 請選擇上方心法開始研讀")
    else:
        st.subheader(f"📍 當前課程：{curr}")
        
        # --- 功能細節區 ---
        
        if "一." in curr:
            st.markdown("""
            * **趨勢大方向**：建議用年線畫趨勢線，找大波段低點。
            * **1分線操作**：找50點波動，K棒站上 20MA 爆量買入。
            """)
            # 預留圖片位置：請將圖片命名為 notes_1.jpg 並上傳到 GitHub
            try:
                st.image("notes_1.jpg", caption="心法一：趨勢線範例圖")
            except:
                st.warning("📷 圖片 notes_1.jpg 尚未上傳，請將圖片放入 GitHub 專案中。")

        elif "二." in curr or "三." in curr:
            # 箱型計算機
            col_in1, col_in2 = st.columns(2)
            with col_in1: hp = st.number_input("箱型最高 (壓力)", value=100.0)
            with col_in2: lp = st.number_input("箱型最低 (支撐)", value=90.0)
            
            diff = hp - lp
            mid = lp + (diff / 2)
            
            c1, c2, c3 = st.columns(3)
            c1.metric("🛡️ 中軸守備線", f"{mid:.2f}")
            c2.metric("🚀 第二波目標", f"{hp + diff:.2f}")
            c3.metric("📉 停損/回檔位", f"{lp - diff:.2f}")
            
            st.write("1. **波段定義**：爆量點至整理區為一波。2. **箱型加碼**：突破且站穩 20MA。")
            try:
                st.image("notes_2.jpg", caption="心法二：箱型繪製教學")
            except:
                st.info("📷 圖片載入中 (等待上傳 notes_2.jpg)")

        elif "四." in curr:
            st.write("1. **60MA 轉折**：1H 跌破 60MA 先撤。2. **200MA 長線**：5分線站上 200MA 做多。")

        elif "七." in curr:
            # 資金分配計算
            total = st.number_input("您的總資產 (萬元)", value=100.0)
            st.write(f"📊 **資產配置建議：**")
            st.info(f"60% 高股息: {total*0.6:.1f}萬 | 30% 波動型: {total*0.3:.1f}萬 | 10% 短線: {total*0.1:.1f}萬")

        elif "九." in curr:
            st.error("⚠️ 緊急下跌保命符")
            with st.expander("🛠️ 加碼/出場 診斷清單", expanded=True):
                st.checkbox("1. 5分
