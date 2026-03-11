import streamlit as st

# 1. 頁面配置
st.set_page_config(page_title="股票心法 VIP 系統", layout="wide", page_icon="📈")

# 2. 初始化登入狀態與選單
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'current_tab' not in st.session_state:
    st.session_state['current_tab'] = "主目錄"

# --- 側邊欄：帳號登入 ---
with st.sidebar:
    st.title("🔐 會員登入")
    if not st.session_state['logged_in']:
        user_id = st.text_input("帳號", placeholder="admin")
        user_pw = st.text_input("密碼", type="password", placeholder="888888")
        if st.button("登入系統", use_container_width=True):
            if user_id == "admin" and user_pw == "888888":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("帳密錯誤")
    else:
        st.success("✅ VIP 會員已登入")
        if st.button("登出"):
            st.session_state['logged_in'] = False
            st.session_state['current_tab'] = "主目錄"
            st.rerun()
    st.divider()
    st.info("💡 專業建議：紀律是獲利的唯一路徑。")

# --- 主頁面佈局 ---
left_spacer, main_content, right_spacer = st.columns([1, 2, 1])

with main_content:
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📈 股票心法 VIP 專屬系統</h1>", unsafe_allow_html=True)
    st.write("---")

    # 目錄定義
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

    # 顯示目錄按鈕
    for i, item in enumerate(menu_items):
        if st.button(item, key=f"menu_{i}", use_container_width=True):
            st.session_state['current_tab'] = item

    st.write("---")
    
    # --- 內容顯示區 (權限控管) ---
    tab = st.session_state['current_tab']
    
    if tab != "主目錄":
        if st.session_state['logged_in']:
            st.subheader(f"📍 當前功能：{tab}")
            
            # --- 功能實作：箱型波段 (心法二 & 三) ---
            if "箱型" in tab:
                st.markdown("#### 🎯 專業箱型波段預測器")
                c1, c2 = st.columns(2)
                high_p = c1.number_input("箱型最高 (壓力)", value=100.0)
                low_p = c2.number_input("箱型最低 (支撐)", value=80.0)
                
                box_h = high_p - low_p
                mid_p = low_p + (box_h / 2)
                target = high_p + box_h
                
                res1, res2, res3 = st.columns(3)
                res1.metric("箱型高度", f"{box_h:.2f}")
                res2.metric("🛡️ 中位線", f"{mid_p:.2f}")
                res3.metric("🚀 第二波目標", f"{target:.2f}")
                st.warning(f"💡 心法提醒：股價在 {mid_p} 以下進場勝率較高，波動較小。")

            # --- 功能實作：資金分配 (心法七) ---
            elif "資金分配" in tab:
                st.markdown("#### 💰 6-3-1 資金管理工具")
                total_money = st.number_input("請輸入總可用資金 (萬元)", value=100.0, step=10.0)
                
                f1, f2, f3 = st.columns(3)
                f1.metric("60% 高股息 ETF", f"{total_money * 0.6:.1f}萬")
                f2.metric("30% 波動型 ETF", f"{total_money * 0.3:.1f}萬")
                f3.metric("10% 短線個股", f"{total_money * 0.1:.1f}萬")
                
                st.write("---")
                st.write("🧪 **個股分配 (10%) 試算：**")
                stock_count = st.slider("預計持有幾檔個股？", 1, 10, 10)
                per_stock =
