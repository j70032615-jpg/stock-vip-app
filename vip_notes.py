import streamlit as st
import pandas as pd

# ==========================================
# 核心設定區：請確認 SHEET_ID 與 SHEET_NAME 正確
# ==========================================
# 您的試算表 ID
SHEET_ID = "1oWgZi4LPnYfwe22sG2MJOzZCj1LkUXysQ-pAG-3Pr98"
# 這裡改回中文，最直覺也最不容易出錯
SHEET_NAME = "VIP名單" 

# 建立 Google Sheets CSV 讀取連結
URL_USERS = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

st.set_page_config(page_title="股票十大心法 VIP 系統", layout="wide")

# 初始化登入狀態
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- 登入介面 ---
if not st.session_state.logged_in:
    st.title("🔐 股票十大心法 VIP 系統")
    st.info("請輸入您的 VIP 帳號密碼以解鎖核心內容。")
    
    with st.form("login_form"):
        input_user = st.text_input("VIP 帳號")
        input_pw = st.text_input("登入密碼", type="password")
        submit_button = st.form_submit_button("登入系統")
        
        if submit_button:
            try:
                # 讀取雲端資料
                users_df = pd.read_csv(URL_USERS)
                
                # 究極防呆比對邏輯
                is_vip = False
                input_u_str = str(input_user).strip()
                input_p_str = str(input_pw).strip()
                
                for index, row in users_df.iterrows():
                    # 抓第一欄與第二欄
                    db_u = str(row[0]).strip()
                    db_p = str(row[1]).strip()
                    
                    if input_u_str == db_u and input_p_str == db_p:
                        is_vip = True
                        break
                
                if is_vip:
                    st.session_state.logged_in = True
                    st.success("驗證成功！正在解鎖心法...")
                    st.rerun()
                else:
                    st.error("❌ 帳號或密碼錯誤，請重新輸入。")
            except Exception as e:
                st.error(f"連線失敗：請確認試算表已「發布到網路」")
                st.info(f"技術提醒：請檢查試算表分頁名稱是否為『{SHEET_NAME}』")

# --- 核心心法內容區 ---
else:
    st.sidebar.success("✅ VIP 已登入")
    if st.sidebar.button("登出系統"):
        st.session_state.logged_in = False
        st.rerun()

    st.title("📈 股票十大心法核心內容")
    
    tab1, tab2, tab3 = st.tabs(["核心心法", "緊急狀況處理", "資金分配"])

    with tab1:
        st.header("一. 畫趨勢線與心法操作順序")
        st.markdown("""
        1. **畫趨勢線**：建議直接用年線去畫，找到大方向跟最低價位。
        2. **爆量位置**：容易看到爆量下影線的位置。
        3. **進場準則**：K棒在 20MA 爆量上漲進場。
        4. **出場準則**：K棒爆量跌破 5MA 出場。
        5. **箱型確認**：1小時線 20日線突破或跌破需畫箱型確認。
        """)

    with tab2:
        st.header("二. 緊急下跌狀況提醒")
        st.warning("⚠️ 避免操作錯誤的檢查清單：")
        st.markdown("""
        1. **加碼判斷**：看 1分或5分線的 200MA 是否站上突破。
        2. **結算日風險**：期貨結算日機率性持續下跌。
        3. **量能監控**：看量是否放大且跌破最低點。
        4. **早盤守線**：15分線早盤最大量 K 棒不可跌破。
        5. **中期轉折**：1小時線 60MA 跌破先出場。
        """)

    with tab3:
        st.header("三. 資金分配策略")
        st.markdown("""
        * **60% 資金**：挑選 2 檔高股息 ETF (如 00919, 0056)。
        * **30% 資金**：挑選 1 檔波動型 ETF。
        * **10% 資金**：短線個股或緊急預備金。
        * **獲利機制**
