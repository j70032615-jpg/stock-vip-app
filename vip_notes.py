import streamlit as st

# 1. 頁面基礎設定
st.set_page_config(
    page_title="股票心法 VIP 專屬系統",
    page_icon="📈",
    layout="wide"
)

# 2. 左側邊欄：登入介面
with st.sidebar:
    st.markdown("## 🔐 會員登入")
    user_id = st.text_input("會員帳號", placeholder="請輸入帳號", key="user_id")
    user_pw = st.text_input("會員密碼", type="password", placeholder="請輸入密碼", key="user_pw")
    
    if st.button("立即進入系統", use_container_width=True):
        if user_id and user_pw:
            st.success(f"歡迎回來，{user_id}！")
        else:
            st.warning("請輸入帳號與密碼")

    st.divider()
    st.info("💡 **專業建議**：\n紀律是獲利的唯一路徑。")

# 3. 主頁面：置中目錄設計
left_spacer, main_content, right_spacer = st.columns([1, 2, 1])

with main_content:
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📈 股票心法目錄</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>VIP 專屬實戰策略系統</p>", unsafe_allow_html=True)
    st.write("---")
    
    # 目錄清單內容
    menu_items = [
        "一. 畫趨勢線確認位置",
        "二. 畫箱型 + 波段 + 壓力支撐線",
        "三. 用箱形突破找加碼點跟出場點",
        "四. 均線做法",
        "五. 懶人高勝法",
        "六. 單純找裸K選股",
        "七. 資金分配法",
        "八. 精準支撐壓力",
        "九. 緊急下跌狀況注意提醒"
    ]
    
    # 產生美觀按鈕
    for i, item in enumerate(menu_items):
        if st.button(item, key=f"menu_{i}", use_container_width=True):
            st.toast(f"載入中：{item}")
            st.subheader(f"📍 當前選取：{item}")
            st.write("正在連接數據庫，請稍候...")

    st.write("---")
    st.caption("© 2026 股票心法 VIP 專屬系統 | 核心開發：比爾蓋茲")
