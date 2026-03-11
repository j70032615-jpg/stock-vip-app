import streamlit as st

# 1. 設定頁面配置 (寬螢幕模式，符合專業看盤習慣)
st.set_page_config(page_title="股票心法 VIP 系統", layout="wide")

# 2. 左側導覽列：帳號密碼與系統狀態
with st.sidebar:
    st.title("🔐 會員登入")
    user_id = st.text_input("會員帳號", placeholder="請輸入帳號")
    user_pw = st.text_input("會員密碼", type="password", placeholder="請輸入密碼")
    
    if st.button("立即進入系統", use_container_width=True):
        # 這裡保留你原本的驗證邏輯
        st.success("驗證中...")

    st.divider()
    st.info("💡 專業建議：定期更改密碼以保護您的交易心法。")

# 3. 主頁面：股票心法目錄
# 使用 columns 讓內容居中，視覺上更平衡
left_space, main_content, right_space = st.columns([1, 2, 1])

with main_content:
    st.markdown("<h1 style='text-align: center;'>📈 股票心法目錄</h1>", unsafe_allow_code=True)
    st.write("---")
    
    # 定義目錄內容
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
    
    # 使用 Button 或 Expander 呈現，這裡先用美化的清單
    for item in menu_items:
        st.button(item, use_container_width=True)

    st.write("---")
    st.caption("© 2026 股票心法 VIP 專屬系統 | 核心開發：Gemini-比爾蓋茲版")
