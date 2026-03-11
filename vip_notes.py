import streamlit as st

# 1. 頁面基礎配置
st.set_page_config(page_title="股票心法 VIP 系統", layout="wide", page_icon="📈")

# 2. 初始化 Session State (確保狀態不丟失)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'current_tab' not in st.session_state:
    st.session_state['current_tab'] = "主目錄"

# --- 側邊欄：VIP 登入驗證 ---
with st.sidebar:
    st.title("🔐 會員登入")
    if not st.session_state['logged_in']:
        u_id = st.text_input("帳號", placeholder="admin")
        u_pw = st.text_input("密碼", type="password", placeholder="888888")
        if st.button("確認進入系統", use_container_width=True):
            if u_id == "admin" and u_pw == "888888":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("帳號或密碼錯誤")
    else:
        st.success("✅ VIP 權限已啟動")
        if st.button("登出系統", use_container_width=True):
            st.session_state['logged_in'] = False
            st.session_state['current_tab'] = "主目錄"
            st.rerun()
    st.divider()
    st.caption("核心技術支援：比爾蓋茲")

# --- 主區塊：目錄與內容 ---
left_sp, main_col, right_sp = st.columns([1, 2, 1])

with main_col:
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📈 股票心法 VIP 專屬系統</h1>", unsafe_allow_html=True)
    st.write("---")

    # 目錄清單
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

    # 生成目錄按鈕 (所有人可見)
    for i, item in enumerate(menu_items):
        if st.button(item, key=f"btn_{i}", use_container_width=True):
            st.session_state['current_tab'] = item

    st.write("---")

    # --- VIP 核心內容區域 ---
    current_tab = st.session_state['current_tab']
    
    if current_tab != "主目錄":
        if st.session_state['logged_in']:
            st.subheader(f"📍 當前實戰工具：{current_tab}")
            
            # 實作：箱型波段預測 (心法二、三)
            if "箱型" in current_tab:
                st.markdown("#### 🎯 專業箱型目標價預測")
                c1, c2 = st.columns(2)
                h_p = c1.number_input("箱型最高價 (壓力線)", value=100.0)
                l_p = c2.number_input("箱型最低價 (支撐線)", value=80.0)
                
                # 核心公式 (隱藏在後端)
                box_h = h_p - l_p
                mid_p = l_p + (box_h / 2)
                target_1 = h_p + box_h
                
                m1, m2, m3 = st.columns(3)
                m1.metric("📦 箱型高度", f"{box_h:.2f}")
                m2.metric("🛡️ 強弱中軸線", f"{mid_p:.2f}")
                m3.metric("🚀 第二波目標", f"{target_1:.2f}")
                st.info(f"💡 專業建議：股價在 {mid_p} 以下進場風險較小，突破 {h_p} 為加碼點。")

            # 實作：資金分配 (心法七)
            elif "資金分配" in current_tab:
                st.markdown("#### 💰 6-3-1 專業資金管理")
                total_m = st.number_input("請輸入總資產 (單位：萬元)", value=100.0, step=10.0)
                
                f1, f2, f3 = st.columns(3)
                f1.metric("60% 高股息 ETF", f"{total_m * 0.6:.1f}萬")
                f2.metric("30% 波動型 ETF", f"{total_m * 0.3:.1f}萬")
                f3.metric("10% 短線個股", f"{total_m * 0.1:.1f}萬")
                
                st.divider()
                st.write("🧪 **個股分配試算：**")
                s_count = st.slider("預計持有幾檔短線個股？", 1, 10, 5)
                per_s = (total_m * 0.1) / s_count
                st.success(f"建議每檔個股投入金額： **{per_s:.2f} 萬元**")
            
            else:
                st.info(f"「{current_tab}」模組正在全力數位化中，請稍候。")
        else:
            st.warning("🔒 此功能內含核心公式，僅限 VIP 會員登入後查看。")

    st.write("---")
    st.caption("© 2026 股票心法 VIP | 紀律是唯一通往財富的道路")
