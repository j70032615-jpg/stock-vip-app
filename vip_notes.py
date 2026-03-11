import streamlit as st

# 1. 頁面配置
st.set_page_config(page_title="股票心法 VIP 系統", layout="wide", page_icon="📈")

# 2. 初始化登入狀態
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

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
        st.success("✅ VIP 已登入")
        if st.button("登出"):
            st.session_state['logged_in'] = False
            st.rerun()
    st.divider()
    st.caption("核心開發：比爾蓋茲")

# --- 主頁面佈局 ---
left_spacer, main_content, right_spacer = st.columns([1, 2, 1])

with main_content:
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📈 股票心法 VIP 目錄</h1>", unsafe_allow_html=True)
    st.write("---")

    # 定義目錄
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

    # 顯示目錄按鈕 (所有人都能看到目錄)
    for i, item in enumerate(menu_items):
        if st.button(item, key=f"menu_{i}", use_container_width=True):
            st.session_state['current_tab'] = item

    # --- VIP 內容顯示區 ---
    st.write("---")
    current_tab = st.session_state.get('current_tab', None)

    if current_tab:
        if st.session_state['logged_in']:
            st.subheader(f"📍 {current_tab}")
            
            # 實作「二」與「三」的箱型計算邏輯 (核心技術轉換)
            if "箱型" in current_tab:
                st.markdown("#### 🎯 專業箱型波段預測器")
                c1, c2 = st.columns(2)
                with c1:
                    high_p = st.number_input("箱型最高 (壓力)", value=100.0)
                with c2:
                    low_p = st.number_input("箱型最低 (支撐)", value=80.0)
                
                # 公式計算 (防盜鎖死在後端)
                box_h = high_p - low_p
                mid_p = low_p + (box_h / 2)
                target = high_p + box_h
                
                res1, res2, res3 = st.columns(3)
                res1.metric("箱型高度", f"{box_h:.2f}")
                res2.metric("🛡️ 中位線", f"{mid_p:.2f}")
                res3.metric("🚀 目標價", f"{target:.2f}")
                
                st.warning(f"💡 心法提醒：股價在 {mid_p} 以下進場勝率較高，突破 {high_p} 追下一波段。")
            
            else:
                st.info(f"「{current_tab}」的詳細內容正在數位化中...")
        else:
            st.warning("🔒 此為 VIP 核心心法，請先從左側登入後查看公式與計算工具。")
