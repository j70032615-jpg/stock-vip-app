import streamlit as st
import pandas as pd

# 1. 基礎頁面配置
st.set_page_config(page_title="股票十大心法 VIP 系統", layout="wide", page_icon="📈")

# 2. 狀態初始化 (確保所有功能不跳掉)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "主目錄"

# --- 側邊欄：登入與資安管理 ---
with st.sidebar:
    st.title("🔐 VIP 會員中心")
    if not st.session_state['logged_in']:
        u = st.text_input("輸入 VIP 帳號")
        p = st.text_input("輸入 登入密碼", type="password")
        if st.button("驗證權限進入", use_container_width=True):
            # 這裡就是你的安全名單，你可以隨時往下增加
            VIP_LIST = {
                "1234": "1234",
                "rich88": "win588",
                "guest": "9999"
            }
            if u in VIP_LIST and VIP_LIST[u] == p:
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("❌ 帳密不符，請洽比爾蓋茲")
    else:
        st.success(f"✅ VIP 權限已啟動")
        if st.button("🚪 安全登出系統", use_container_width=True):
            st.session_state['logged_in'] = False
            st.session_state['tab'] = "主目錄"
            st.rerun()
    st.divider()
    st.caption("核心開發：比爾蓋茲 | 2026 穩定版")

# --- 主畫面顯示 ---
# 如果沒登入，只顯示帥氣的封面
if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align: center;'>📈 股票十大心法 VIP 系統</h1>", unsafe_allow_html=True)
    st.info("請於左側登入以開啟核心戰術庫與精算工具。")
else:
    # 登入後顯示的內容
    st.markdown(f"<h1 style='text-align: center; color: #1E88E5;'>核心戰術：{st.session_state['tab']}</h1>", unsafe_allow_html=True)
    st.write("---")

    # 九大心法目錄按鈕 (這就是你最愛的導航)
    menu = [
        "一. 畫趨勢線確認位置", "二. 畫箱型 + 波段 + 壓力支撐線", 
        "三. 用箱形突破找加碼點跟出場點", "四. 均線做法", 
        "五. 懶人穩勝法", "六. 單純找裸K選股", 
        "七. 資金分配法", "八. 精準支撐壓力", 
        "九. 緊急下跌狀況注意提醒"
    ]
    
    # 用 Columns 做出整齊的目錄感
    cols = st.columns(3)
    for i, item in enumerate(menu):
        with cols[i % 3]:
            if st.button(item, key=f"btn_{i}", use_container_width=True):
                st.session_state['tab'] = item

    st.write("---")
    curr = st.session_state['tab']

    # --- 1. 趨勢線 ---
    if "一." in curr:
        st.subheader("📍 趨勢線筆記")
        # 這裡就是放入圖片的地方
        # st.image("你的圖片網址或檔案名稱")
        st.markdown("""
        1. **年線準則**：找歷來平均最高最低點，方向最準。
        2. **1分線波動**：找50點左右波動。K棒在 20MA 爆量上漲進場。
        """)

    # --- 2 & 3. 箱型計算機 (恢復你最愛的工具) ---
    elif "二." in curr or "三." in curr:
        st.subheader("🧮 箱型空間自動精算")
        c1, c2 = st.columns(2)
        with c1: hp = st.number_input("箱型最高 (壓力價)", value=100.0)
        with c2: lp = st.number_input("箱型最低 (支撐價)", value=90.0)
        
        diff = hp - lp
        mid = lp + (diff / 2)
        
        m1, m2, m3 = st.columns(3)
        m1.metric("🛡️ 中軸守備線", f"{mid:.2f}")
        m2.metric("🚀 第二波目標", f"{hp + diff:.2f}")
        m3.metric("📉 跌破回檔位", f"{lp - diff:.2f}")

    # --- 7. 資金分配法 (計算功能全回歸) ---
    elif "七." in curr:
        st.subheader("💰 專業資金水位配置")
        total = st.number_input("輸入擬投入總資產 (萬元)", value=100.0)
        st.write(f"建議配置如下：")
        st.code(f"60% 高股息 (00919/0056): {total*0.6:.1f} 萬\n30% 波動型 (個股/期指): {total*0.3:.1f} 萬\n10% 短線急用預備金: {total*0.1:.1f} 萬")

    # --- 9. 緊急下跌診斷 (保命符全回歸) ---
    elif "九." in curr:
        st.error("🆘 緊急下跌保命清單")
        col_L, col_R = st.columns(2)
        with col_L:
            st.write("### 🟢 加碼條件")
            st.checkbox("1. 1/5分線『突破站上』200MA？")
            st.checkbox("2. 回測『箱型起漲點』未破？")
        with col_R:
            st.write("### 🔴 出場警告")
            st.checkbox("1. 跌破今日 15分線最大量低點？")
            st.checkbox("2. 1小時線 60MA 跌破？")

    # 其他沒寫到的部分顯示建設中
    elif curr != "主目錄":
        st.info(f"正在載入 {curr} 的詳細圖片與筆記...")
        # st.image("你的圖片路徑")

    if curr != "主目錄":
        if st.button("⬅️ 返回主目錄"):
            st.session_state['tab'] = "主目錄"
            st.rerun()
