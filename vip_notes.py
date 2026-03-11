import streamlit as st
import pandas as pd
import requests
from io import StringIO

# 1. 基礎設定 - 請再次確認 SHEET_ID
# 根據你的圖片，你的 SHEET_ID 應該是：1oWgZi4LPnYfwe22sG2MJOzZCj1LkUXysQ-pAG-3Pr98
SHEET_ID = "1oWgZi4LPnYfwe22sG2MJOzZCj1LkUXysQ-pAG-3Pr98"
# 這是你「VIP名單」分頁的 ID，從你第一張圖看是 1834495482
GID = "1834495482" 

# 重新構建一個更穩定的下載網址
URL_CSV = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={GID}"

st.set_page_config(page_title="股票心法 VIP 系統", layout="wide")

if "vip_auth" not in st.session_state:
    st.session_state.vip_auth = False

# --- 登入畫面 ---
if not st.session_state.vip_auth:
    st.title("📈 股票心法 VIP 專屬系統")
    
    with st.container(border=True):
        user_input = st.text_input("會員帳號")
        pw_input = st.text_input("會員密碼", type="password")
        
        if st.button("立即進入系統", use_container_width=True):
            try:
                # 使用 requests 抓取，這比直接用 pd.read_csv 更穩定，能避開很多網路限制
                response = requests.get(URL_CSV)
                response.encoding = 'utf-8'
                
                if response.status_code == 200:
                    df = pd.read_csv(StringIO(response.text)).astype(str)
                    
                    # 這裡會自動過濾掉空格
                    match = False
                    for _, row in df.iterrows():
                        # 比對第一欄(帳號)與第二欄(密碼)
                        if str(user_input).strip() == str(row[0]).strip() and \
                           str(pw_input).strip() == str(row[1]).strip():
                            match = True
                            break
                    
                    if match:
                        st.session_state.vip_auth = True
                        st.success("✅ 登入成功！")
                        st.rerun()
                    else:
                        st.error("❌ 帳號或密碼錯誤（請檢查試算表 A2, B2）")
                else:
                    st.error(f"⚠️ 抓取失敗，錯誤代碼: {response.status_code}。請檢查『發布到網路』是否勾選了全份文件。")
            
            except Exception as e:
                st.error(f"⚠️ 系統連線異常: {e}")
                st.info("💡 工程師提示：請確認您的 Google 試算表權限為『知道連結的所有人皆可檢視』")

# --- 登入後的內容 ---
else:
    st.sidebar.success("VIP 權限已啟動")
    if st.sidebar.button("登出"):
        st.session_state.vip_auth = False
        st.rerun()
        
    st.title("🚀 歡迎回來，VIP 會員")
    st.write("這裡可以開始放入你的教學筆記圖片或文字內容。")
    # 範例：st.image("你的圖片網址")
