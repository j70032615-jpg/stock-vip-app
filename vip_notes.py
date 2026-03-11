import streamlit as st

# 1. 基礎設定
st.set_page_config(page_title="股票心法 VIP 系統", layout="wide", page_icon="📈")

# 2. 狀態初始化
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "九大心法"

# --- 側邊欄：VIP 登入 ---
with st.sidebar:
    st.title("🔐 VIP 會員系統")
    if not st.session_state['logged_in']:
        # 使用你設定的預設密碼 1234
        u = st.text_input("帳號", key="u_input")
        p = st.text_input("密碼", type="password", key="p_input")
        if st.button("確認進入系統", use_container_width=True):
            if u == "1234" and p == "1234":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("密碼錯誤")
    else:
        st.success("✅ VIP 權限已啟動")
        if st.button("📖 完整九大心法", use_container_width=True): 
            st.session_state['tab'] = "九大心法"
        if st.button("🛡️ 12條保命準則", use_container_width=True): 
            st.session_state['tab'] = "保命準則"
        st.divider()
        if st.button("安全登出", use_container_width=True):
            st.session_state['logged_in'] = False
            st.rerun()

# --- 主畫面內容 ---
if not st.session_state['logged_in']:
    st.info("🔒 歡迎來到 VIP 專屬系統，請由左側登入以開啟心法內容。")
else:
    if st.session_state['tab'] == "九大心法":
        st.header("📖 股票心法操作順序 (VIP 完整版)")
        
        with st.expander("一. 畫趨勢線 (找大方向與買點)", expanded=True):
            st.write("1. **建議用年線畫**：找到歷來平均高低點，方向最準，且易見爆量下影線位置。")
            st.write("2. **1分線波動**：找50點左右波動做。K在20MA爆量上漲進場，爆量跌破5MA出場。")
            st.write("3. **空頭避開**：K站在20MA下方，站上又跌破為下跌趨勢，需等爆量站回20MA。")
            st.write("4. **簡單判斷**：持續站在5日線上方為多頭，持續跌破為空頭。")
            st.write("5. **層次法**：先以1小時線畫趨勢線，再用短線找進場位置。")

        with st.expander("二. 畫箱型波段"):
            st.write("1. **一波段定義**：從爆量下影線往上畫至前高整理區。通常漲2-3波，強勢5波。")
            st.write("2. **壓力支撐**：畫完一波即形成箱型，最高與最低即為壓力支撐。")
            st.write("3. **波段確認**：突破箱型需站穩20MA才是新波段；跌破則反之。")

        with st.expander("三. 箱型計算與加碼點"):
            st.subheader("🛡️ 箱型中間值計算器")
            col1, col2 = st.columns(2)
            high_p = col1.number_input("箱型頂部價位", value=100.0)
            low_p = col2.number_input("箱型底部價位", value=90.0)
            mid_p = low_p + ((high_p - low_p) / 2)
            st.metric("關鍵中軸線", f"{mid_p:.2f}", help="跌破中間值需出場")
            
            st.write("---")
            st.write("* **加碼策略**：箱型剛突破可加碼，但要站上20MA。")
            st.write("* **波段聯動**：15分線一波箭頭若400點，未來下跌波段也可能對應400點。")
            st.write("* **分批操作**：底部買兩張，一張長抱，一張按中間值與趨勢線做短線。")

        with st.expander("四. 均線做法"):
            st.write("1. **轉折防線**：1小時線跌破60MA先逃，漲回60MA再買回。")
            st.write("2. **極短線**：期貨5分線突破200MA做多，跌回200MA賣出。")
            st.write("3. **爆量起點**：1分線K在5MA下爆量跌破又漲回，為起漲點。")

        with st.expander("五 ~ 八. 懶人法、裸K與資金配置"):
            st.write("**懶人穩勝**：站上周線20MA/60MA不跌破即為多頭。KDJ月線20下黃金交叉進場。")
            st.write("**裸K選股**：找底部長期短K盤整＋爆量上漲（主力吃貨翻倍訊號）。")
            st.write("**資金分配**：60%高股息ETF、30%波動型ETF、10%短線。獲利20%出10%，跌20%進20%。")

    elif st.session_state['tab'] == "保命準則":
        st.header("🚨 九. 12 條緊急保命準則")
        st.warning("遇到急殺時，請立刻檢查以下各點：")
        st.markdown("""
        1. 加碼前看 1/5 分線 **200MA** 站穩沒。
        2. 跌破當日 **爆量K棒最低點** 必須出場。
        3. 早盤 15 分最大量 K 棒被跌破，盤勢極弱。
        4. 下午盤跌破 **5分線 200MA**，先走為妙。
        5. **1小時 60MA** 或 **周線 20MA** 跌破，波段結束。
        6. **假突破處理**：進場被跌回馬上撤，真突破再買回。
        7. **破底翻**：箱型破底又漲回要趕快買回，那是新波段。
        """)

    st.divider()
    st.caption("核心技術支援：比爾蓋茲 | 心法歸納：VIP 會員")
