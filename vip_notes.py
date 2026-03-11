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
l_sp, m_col, r_sp = st.columns([1, 2, 1])

with m_col:
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📈 股票心法 VIP 系統</h1>", unsafe_allow_html=True)
    st.write("---")

    menu = [
        "一. 畫趨勢線確認位置", "二. 畫箱型 + 波段 + 壓力支撐線", 
        "三. 用箱形突破找加碼點跟出場點", "四. 均線做法", 
        "五. 懶人穩勝法", "六. 單純找裸K選股", 
        "七. 資金分配法", "八. 精準支撐壓力", 
        "九. 緊急下跌狀況注意提醒"
    ]
    
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
                st.write("4. **最簡判斷**：持續站在 5 日線上為多頭，跌破為空頭。")
                st.write("5. **層次**：先以 1 小時線畫趨勢，再用短線找精確進場點。")

            # --- 二 & 三. 箱型邏輯 ---
            elif "二." in curr or "三." in curr:
                hp = st.number_input("箱型最高 (壓力)", value=100.0)
                lp = st.number_input("箱型最低 (支撐)", value=90.0)
                diff = hp - lp
                mid = lp + (diff / 2)
                st.metric("🛡️ 中軸守備線", f"{mid:.2f}")
                st.metric("🚀 第二波目標", f"{hp + diff:.2f}")
                st.write("---")
                st.write("1. **波段定義**：爆量下影線往上至整理區箭頭為一波，通常漲 2-3 波。")
                st.write("2. **箱型加碼**：突破後可加碼，但需站穩 20MA。")
                st.write("3. **波動對應**：15分線一波 400 點，下跌也可能對應 400 點。")

            # --- 四. 均線做法 ---
            elif "四." in curr:
                st.write("1. **60MA 轉折**：1小時跌破 60MA 先逃，漲回買回。")
                st.write("2. **200MA 長線**：期貨5分線突破 200MA 做多，跌回賣。")
                st.write("3. **1分線爆量**：5MA 下爆量跌破又漲回是起漲；5MA 上爆量突破又跌破是起跌。")

            # --- 五 & 六. 懶人與裸K ---
            elif "五." in curr:
                st.write("懶人法：周線 20MA/60MA 守住為多頭；KDJ 月線 20 下金叉買進。")
            elif "六." in curr:
                st.write("裸 K：找底部吃貨短 K 盤整 + 爆量大 K 翻漲。")

            # --- 七. 資金分配 ---
            elif "七." in curr:
                total = st.number_input("總資產 (萬元)", value=100.0)
                st.write(f"💰 60% 高股息: {total*0.6:.1f} 萬")
                st.write(f"💰 30% 波動型: {total*0.3:.1f} 萬")
                st.write(f"💰 10% 短線個股: {total*0.1:.1f} 萬")
                st.info("獲利 20% 出場 10% 資金；跌 20% 進場獲利資金。")

            # --- 八. 精準支撐壓力 ---
            elif "八." in curr:
                st.write("1. 下跌趨勢起始頭部為壓力線 (1H 60MA 跌破後需等待壓力突破)。")
                st.write("2. 上升趨勢起始底部為支撐線。")

            # --- 九. 緊急下跌診斷 ---
            elif "九." in curr:
                st.error("⚠️ 緊急下跌狀況診斷清單 (保命符)")
                with st.expander("🛠️ 【該不該加碼？】"):
                    st.checkbox("1. 1分或5分線是否『突破站上』200MA？")
                    st.checkbox("2. 是否跌回『箱型起漲點』且未跌破？")
                with st.expander("🏃 【該不該出場？】"):
                    st.checkbox("1. 今天是否為『期貨結算日』？")
                    st.checkbox("2. 跌破『今日 15分線最大量 K 棒』最低點？")
                    st.checkbox("3. 1小時線 60MA 或周線 20MA 跌破？")
                st.info("假突破馬上出；破底翻趕快買回。開盤前勿追高。")

        else:
            st.warning("🔒 此為 VIP 專屬內容，請先登入 (1234)。")

    st.write("---")
    st.caption("© 2026 股票心法 VIP | 核心開發：比爾蓋茲")
