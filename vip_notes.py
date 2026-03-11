import streamlit as st

# 1. 基本頁面設定
st.set_page_config(page_title="股票心法 VIP 系統", layout="wide", page_icon="📈")

# 2. 初始化狀態
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "九大心法"

# --- 側邊欄：VIP 登入 ---
with st.sidebar:
    st.title("🔐 VIP 會員系統")
    if not st.session_state['logged_in']:
        # 使用你截圖中的預設帳密 1234
        u = st.text_input("帳號", key="u_login")
        p = st.text_input("密碼", type="password", key="p_login")
        if st.button("確認進入系統", use_container_width=True):
            if u == "1234" and p == "1234":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("密碼錯誤，請重新輸入")
    else:
        st.success("✅ VIP 已登入")
        if st.button("📖 完整九大心法", use_container_width=True): st.session_state['tab'] = "九大心法"
        if st.button("🚨 12條保命準則", use_container_width=True): st.session_state['tab'] = "保命準則"
        st.divider()
        if st.button("安全登出", use_container_width=True):
            st.session_state['logged_in'] = False
            st.rerun()

# --- 主畫面內容 ---
if not st.session_state['logged_in']:
    st.info("🔒 此為 VIP 專屬系統，請由左側登入。")
else:
    if st.session_state['tab'] == "九大心法":
        st.header("📖 股票心法操作順序 (VIP 完整版)")
        
        # 使用分段式的 st.write 避免長字串崩潰
        with st.expander("一. 畫趨勢線 (找方向與最低價)", expanded=True):
            st.write("1. **年線畫法**：年線能找到歷來平均高低點，方向最準，易見爆量下影線位置。")
            st.write("2. **1分線操作**：波動值約 50 點。20MA 爆量上漲進場，爆量跌破 5MA 出場。")
            st.write("3. **空頭警訊**：K 在 20MA 下方，站上又跌破為下跌趨勢，需等爆量站上 20MA。")
            st.write("4. **多空分野**：站在 5 日線上為多頭，跌破 5 日線為空頭。")
            st.write("5. **進場順序**：先用 1 小時線畫趨勢，再用短線找精確進場點。")

        with st.expander("二. 畫箱型波段"):
            st.write("1. **波段定義**：從爆量下影線往上畫至前高整理區。通常漲 2-3 波，強勢可達 5 波。")
            st.write("2. **箱型形成**：畫完一波即形成箱型，箱頂為壓力，箱底為支撐。")
            st.write("3. **趨勢連動**：突破箱型需站穩 20MA 才是新波段；跌破則轉為下跌波段。")

        with st.expander("三. 箱型中間值與加碼點"):
            st.subheader("🛡️ 中間值自動計算器")
            col1, col2 = st.columns(2)
            high_price = col1.number_input("輸入箱型頂部 (例如 100.0)", value=100.0)
            low_price = col2.number_input("輸入箱型底部 (例如 90.0)", value=90.0)
            # 還原你要求的計算邏輯：(100-90)/2 + 90 = 95
            middle = low_price + ((high_price - low_price) / 2)
            st.metric("核心守備線 (中間值)", f"{middle:.2f}", delta="跌破此線必出場")
            
            st.write("---")
            st.write("* **加碼策略**：箱型剛突破可加碼，但需配合站上 20MA。")
            st.write("* **400點波段**：15分線一波箭頭若為 400 點，則下跌波段通常也對應 400 點。")
            st.write("* **分批買法**：底部買兩張（長/短分開），一張長抱，一張按中間值與趨勢線操作。")

        with st.expander("四 ~ 八. 均線、裸K與資金分配"):
            st.write("**均線做法**：1小時跌破 60MA 先撤；5分線突破 200MA 做多，跌回賣。")
            st.write("**懶人法**：站上周線 20MA/60MA 不跌破即為多頭。KDJ 月線 20 以下金叉進場。")
            st.write("**裸K選股**：找底部長期橫盤 + 爆量上漲，這是有翻倍潛力的主力股。")
            st.write("**資金分配**：60% 高股息、30% 波動型、10% 短線。獲利 20% 出 10% 資金。")

    elif st.session_state['tab'] == "保命準則":
        st.header("🚨 九. 12 條緊急保命準則")
        st.error("保護本金是唯一目標：")
        st.write("1. 加碼前確認 1/5 分線 200MA 是否站穩。")
        st.write("2. 跌破當日「爆量K棒最低點」必須出場。")
        st.write("3. 早盤 15 分最大量 K 棒被跌破，當日盤勢極弱。")
        st.write("4. 下午盤跌破 5分線 200MA，先走為妙。")
        st.write("5. 1小時 60MA 或周線 20MA 跌破，波段行情結束。")
        st.write("6. 假突破進場被跌回馬上下，等真突破再說。")
        st.write("7. 箱型破底翻要追回，否則會少賺一整箱的波段。")
