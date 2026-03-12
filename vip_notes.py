import streamlit as st

# 1. 頁面配置 (保持不變)
st.set_page_config(page_title="股票心法 VIP 系統", layout="wide", page_icon="📈")

# 2. 狀態初始化 (確保選單狀態不遺失)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "主目錄"

# --- 側邊欄：登入與導航 ---
with st.sidebar:
    st.title("🔐 會員登入")
    if not st.session_state['logged_in']:
        u = st.text_input("帳號")
        p = st.text_input("密碼", type="password")
        if st.button("確認進入系統", use_container_width=True):
            # 這裡你可以選用寫死的 "1234" 或我昨晚幫你寫的 Google 試算表連線
            if u == "1234" and p == "1234":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("帳號或密碼錯誤")
    else:
        st.success("✅ VIP 權限已啟動")
        if st.sidebar.button("登出系統", use_container_width=True):
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

    # 九大心法目錄按鈕
    menu = [
        "一. 畫趨勢線確認位置", "二. 畫箱型 + 波段 + 壓力支撐線", 
        "三. 用箱形突破找加碼點跟出場點", "四. 均線做法", 
        "五. 懶人穩勝法", "六. 單純找裸K選股", 
        "七. 資金分配法", "八. 精準支撐壓力", 
        "九. 緊急下跌狀況注意提醒"
    ]
    
    # 建立目錄按鈕
    for i, item in enumerate(menu):
        if st.button(item, key=f"menu_{i}", use_container_width=True):
            st.session_state['tab'] = item

    st.write("---")

    # --- VIP 內容顯示區 ---
    curr = st.session_state['tab']
    
    if curr != "主目錄":
        if st.session_state['logged_in']:
            st.subheader(f"📍 當前位置：{curr}")
            
            # --- 一. 畫趨勢線 ---
            if "一." in curr:
                st.write("### 趨勢線 - 找方向與最低價位 (建議年線)")
                st.write("1. **年線準則**：找歷來平均最高最低點，方向最準，易見爆量下影線。")
                st.write("2. **1分線波動**：找50點左右波動做。K棒在 20MA 爆量上漲進場，跌破 5MA 出場。")
                st.write("3. **空頭避開**：K 在 20MA 下方，站上又跌破為走跌，需等爆量站回 20MA。")

            # --- 二 & 三. 箱型邏輯 (計算功能全回歸) ---
            elif "二." in curr or "三." in curr:
                col_a, col_b = st.columns(2)
                with col_a:
                    hp = st.number_input("箱型最高 (壓力)", value=100.0)
                with col_b:
                    lp = st.number_input("箱型最低 (支撐)", value=90.0)
                
                diff = hp - lp
                mid = lp + (diff / 2)
                
                c1, c2 = st.columns(2)
                c1.metric("🛡️ 中軸守備線", f"{mid:.2f}")
                c2.metric("🚀 第二波目標", f"{hp + diff:.2f}")
                
                st.write("---")
                st.write("1. **波段定義**：爆量下影線往上至整理區箭頭為一波，通常漲 2-3 波。")
                st.write("2. **箱型加碼**：突破後可加碼，但需站穩 20MA。")

            # --- 七. 資金分配 (計算功能全回歸) ---
            elif "七." in curr:
                total = st.number_input("總資產 (萬元)", value=100.0)
                c1, c2, c3 = st.columns(3)
                c1.metric("高股息 (60%)", f"{total*0.6:.1f}萬")
                c2.metric("波動型 (30%)", f"{total*0.3:.1f}萬")
                c3.metric("短線 (10%)", f"{total*0.1:.1f}萬")
                st.info("獲利 20% 出場 10% 資金；跌 20% 進場獲利資金。")

            # --- 九. 緊急下跌診斷 (保命符全回歸) ---
            elif "九." in curr:
                st.error("⚠️ 緊急下跌狀況診斷清單 (保命符)")
                with st.expander("🛠️ 【該不該加碼？】", expanded=True):
                    st.checkbox("1. 1分或5分線是否『突破站上』200MA？")
                    st.checkbox("2. 是否跌回『箱型起漲點』且未跌破？")
                with st.expander("跑 🏃 【該不該出場？】", expanded=True):
                    st.checkbox("1. 今天是否為『期貨結算日』？")
                    st.checkbox("2. 跌破『今日 15分線最大量 K 棒』最低點？")
                    st.checkbox("3. 1小時線 60MA 或周線 20MA 跌破？")

            # ... 其餘 4, 5, 6, 8 項依此類推 ...
            
            if st.button("返回主目錄"):
                st.session_state['tab'] = "主目錄"
                st.rerun()
        else:
            st.warning("🔒 此為 VIP 專屬內容，請先由側邊欄登入。")

    st.write("---")
    st.caption("© 2026 股票心法 VIP | 核心開發：比爾蓋茲")
