import streamlit as st

# 1. 頁面基礎配置
st.set_page_config(page_title="股票心法 VIP 系統", layout="wide", page_icon="📈")

# 2. 狀態初始化
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "主目錄"

# --- 側邊欄：登入與導覽 ---
with st.sidebar:
    st.title("🔐 VIP 會員登入")
    if not st.session_state['logged_in']:
        # 這裡設定你截圖中提到的預設密碼 1234
        u = st.text_input("帳號", key="user_input")
        p = st.text_input("密碼", type="password", key="pass_input")
        if st.button("確認進入系統", use_container_width=True):
            if u == "1234" and p == "1234":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("帳號或密碼錯誤")
    else:
        st.success("✅ VIP 權限已啟動")
        if st.button("📖 完整九大心法", use_container_width=True):
            st.session_state['tab'] = "九大心法"
        if st.button("🛡️ 12條保命準則", use_container_width=True):
            st.session_state['tab'] = "保命準則"
        st.divider()
        if st.button("登出系統", use_container_width=True):
            st.session_state['logged_in'] = False
            st.session_state['tab'] = "主目錄"
            st.rerun()

# --- 主畫面 ---
if not st.session_state['logged_in']:
    st.info("🔒 歡迎來到 VIP 專屬系統，請由左側登入以查看核心心法。")
    st.image("https://images.unsplash.com/photo-1611974717482-482bc676997a?auto=format&fit=crop&q=80&w=2000") # 裝飾用背景
else:
    if st.session_state['tab'] == "九大心法":
        st.header("📖 股票心法操作順序 (100% 完整版)")
        
        with st.expander("一. 畫趨勢線 (找方向與最低點)", expanded=True):
            st.write("""
            1. **建議年線畫法**：年線能找到歷來平均高低點，方向最準，且容易觀察爆量下影線位置。
            2. **1分線操作**：波動值約50點。K棒在20MA爆量上漲進場，爆量跌破5MA出場。
            3. **趨勢判斷**：K棒站在20MA下方，站上又跌破視為下跌趨勢，需等爆量站上20MA。
            4. **5日線邏輯**：持續站在5日線上為多頭，持續跌破為空頭。
            5. **操作順序**：先以1小時線畫趨勢，再用短線尋找進場位置。
            """)

        with st.expander("二. 畫箱型與波段"):
            st.write("""
            1. **一波段定義**：從爆量下影線往上畫至前高整理區。通常漲2-3波，強勢股可達5波。
            2. **壓力支撐**：箱型最高點即為壓力，最低點為支撐。
            3. **均線配合**：箱型突破需站穩20MA才是新波段；跌破20MA則是新的下跌波段。
            """)

        with st.expander("三. 箱型中間值與加碼點"):
            st.write("### 中間值守備法則")
            # 實作計算工具
            c1, c2 = st.columns(2)
            h_val = c1.number_input("箱頂價位", value=100.0)
            l_val = c2.number_input("箱底價位", value=90.0)
            mid = l_val + ((h_val - l_val) / 2)
            st.success(f"💡 此箱型中間值為：{mid:.2f} (跌破此線需考慮出場)")
            
            st.write("""
            * **加碼邏輯**：箱型突破後可加碼，但必須配合站上20MA。
            * **短線計算**：若15分鐘線一波箭頭為400點，未來下跌也可能以400點為一波。
            * **分批操作**：底部可買兩張，一張放長，一張按趨勢線與中間值做短。
            """)

        with st.expander("四. 均線實戰做法"):
            st.write("""
            1. **60MA轉折**：1小時線跌破60MA先撤，漲回買回。
            2. **200MA防線**：極短線5分線突破200MA做多，跌回200MA賣。
            3. **4小時線**：跌破20MA可能下測60MA或200MA。
            4. **盤整訊號**：20MA與K棒頻繁糾結即為盤整，周線級別盤整跌破常伴隨股災。
            """)

        with st.expander("五 ~ 八
