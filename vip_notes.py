import streamlit as st

# --- 1. 基礎頁面配置 ---
st.set_page_config(page_title="股票十大心法 VIP 系統", layout="wide", page_icon="📈")

# 初始化狀態
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "主目錄"

# --- 2. 側邊欄：登入系統 ---
with st.sidebar:
    st.title("🔐 會員登入")
    if not st.session_state['logged_in']:
        u = st.text_input("VIP 帳號")
        p = st.text_input("登入密碼", type="password")
        if st.button("確認進入系統", use_container_width=True):
            # 這裡設定你的帳密
            if u == "1234" and p == "1234":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("❌ 帳號或密碼錯誤")
    else:
        st.success("✅ VIP 權限已啟動")
        if st.sidebar.button("登出系統", use_container_width=True):
            st.session_state['logged_in'] = False
            st.session_state['tab'] = "主目錄"
            st.rerun()
    st.divider()
    st.caption("技術支援：比爾蓋茲 | 2026 版")

# --- 3. 主畫面邏輯 ---
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📈 股票十大心法 VIP 系統</h1>", unsafe_allow_html=True)
st.write("---")

if not st.session_state['logged_in']:
    st.info("💡 請由左側登入以開啟核心戰術庫與精算工具。")
else:
    # 目錄按鈕
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
            if st.button(item, key=f"menu_{i}", use_container_width=True):
                st.session_state['tab'] = item

    st.write("---")
    curr = st.session_state['tab']

    if curr == "主目錄":
        st.write("### 👈 請選擇上方心法按鈕開始學習")
    else:
        st.subheader(f"📍 當前位置：{curr}")
        
        # --- 一. 畫趨勢線 ---
        if "一." in curr:
            st.markdown("1. **年線準則**：找大波段低點。2. **20MA 爆量**：站上則進。")
            try:
                st.image("notes_1.jpg") # 如果你有上傳圖片
            except:
                st.caption("暫無圖片 notes_1.jpg")

        # --- 二 & 三. 箱型計算機 ---
        elif "二." in curr or "三." in curr:
            c1, c2 = st.columns(2)
            with c1: hp = st.number_input("箱型最高", value=100.0)
            with c2: lp = st.number_input("箱型最低", value=90.0)
            diff = hp - lp
            st.metric("🛡️ 中軸守備線", f"{lp + (diff / 2):.2f}")
            st.metric("🚀 第二波目標", f"{hp + diff:.2f}")

        # --- 七. 資金分配 ---
        elif "七." in curr:
            total = st.number_input("總資產 (萬元)", value=100.0)
            st.write(f"💰 60% 高股息: {total*0.6:.1f}萬 | 30% 波動型: {total*0.3:.1f}萬")

        # --- 九. 緊急下跌 (修正 109 行語法錯誤處) ---
        elif "九." in curr:
            st.error("🆘 緊急下跌診斷")
            # 這裡就是你原本出錯的地方，我幫你補齊了引號
            with st.expander("🛠️ 加碼檢查", expanded=True):
                st.checkbox("1. 5分線是否站上 200MA？")
                st.checkbox("2. 回測箱型起漲點未破？")
            with st.expander("🏃 出場檢查", expanded=True):
                st.checkbox("1. 跌破今日 15分線最大量 K 棒低點？")
                st.checkbox("2. 1小時線 60MA 跌破？")

        if st.button("⬅️ 返回主目錄"):
            st.session_state['tab'] = "主目錄"
            st.rerun()

st.write("---")
st.caption("© 2026 股票心法 VIP | 檔案版本：Stable_v1.0")
