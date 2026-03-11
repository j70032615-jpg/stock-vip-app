import streamlit as st
import pandas as pd

# 1. 基礎設定：這是您的試算表身分證，絕對不能少
SHEET_ID = "1oWgZi4LPnYfwe22sG2MJOzZCj1LkUXysQ-pAG-3Pr98"

# 2. 定位分頁：一個抓心法(gid=926157347)，一個抓VIP名單(用分頁名稱)
URL_CONTENT = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid=926157347"
URL_USERS = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet=VIP名單"

def run_pro_app():
    st.set_page_config(page_title="股票十大心法 VIP 系統", layout="wide")
    
    # --- 側邊欄：登入系統 ---
    st.sidebar.title("🔐 會員登入")
    input_user = st.sidebar.text_input("輸入帳號")
    input_pw = st.sidebar.text_input("輸入密碼", type="password")
    
    is_vip = False
    
    if input_user and input_pw:
        try:
            # 讀取雲端 VIP 名單
            users_df = pd.read_csv(URL_USERS)
            users_df.columns = users_df.columns.astype(str).str.strip()
            
            # 比對帳號與密碼 (比對 A 欄與 B 欄)
            match = users_df[(users_df.iloc[:, 0].astype(str) == input_user) & 
                             (users_df.iloc[:, 1].astype(str) == input_pw)]
            
            if not match.empty:
                is_vip = True
                st.sidebar.success(f"✅ 歡迎回來！")
            else:
                st.sidebar.error("❌ 帳號或密碼錯誤")
        except:
            st.sidebar.warning("請確認『VIP名單』分頁已正確發布且名稱無誤。")

    # --- 主畫面：顯示內容 ---
    st.title("🛡️ 股票十大心法 VIP 系統")
    st.write("---")

    try:
        # 讀取心法內容，header=None 確保第一項「一.」不消失
        df = pd.read_csv(URL_CONTENT, header=None)
        
        if not df.empty:
            for i in range(len(df)):
                title = str(df.iloc[i, 0]).strip()
                if title == "nan" or not title: continue
                
                with st.expander(f"📌 {title}"):
                    if is_vip:
                        # 解鎖 B 欄內容與 C 欄圖片
                        st.write(df.iloc[i, 1])
                        img_url = df.iloc[i, 2] if df.shape[1] > 2 else None
                        if isinstance(img_url, str) and img_url.startswith("http"):
                            st.image(img_url, use_container_width=True)
                    else:
                        st.warning("🔒 此為 VIP 專屬內容，請登入查看。")
        else:
            st.info("目前尚無心法數據。")
    except Exception as e:
        st.error(f"連線異常，請確認分頁名稱是否為『心法目錄』。")

if __name__ == "__main__":
    run_pro_app()