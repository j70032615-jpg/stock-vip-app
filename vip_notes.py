import streamlit as st

# 1. 頁面配置
st.set_page_config(page_title="股票心法 VIP 系統", layout="wide")

# 2. 狀態初始化
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "主目錄"

# --- 側邊欄：登入 ---
with st.sidebar:
    st.title("🔐 會員登入")
    if not st.session_state['logged_in']:
        u = st.text_input("帳號")
        p = st.text_input("密碼", type="password")
        if st.button("確認進入系統", use_container_width=True):
            if u == "1234" and p == "1234":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("帳號或密碼錯誤")
    else:
        st.success("✅ VIP 權限已啟動")
        if st.button("登出系統", use_container_width=True):
            st.session_state['logged_in'] = False
            st.session_state['tab'] = "主目錄"
            st.rerun()
    st.divider()
    st.caption("核心技術支援：比爾蓋茲")

# --- 主畫面佈局 ---
l_sp, m_col, r_sp = st.columns([1, 2, 1])

with m_col:
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📈 股票心法 VIP 系統</h1>", unsafe_allow_html=True)
    st.write("---")

    menu = [
        "一. 畫趨勢線確認位置", 
        "二. 畫箱型 + 波段 + 壓力支撐線", 
        "三. 用箱形突破找加碼點跟出場點", 
        "四. 均線做法", 
        "五. 懶人穩勝法", 
        "六. 單純找裸K選股", 
        "七. 資金分配法", 
        "八. 精準支撐壓力", 
        "九. 緊急下跌狀況注意提醒"
    ]
    
    for i, item in enumerate(menu):
        if st.button(item, key=f"menu_{i}", use_container_width=True):
            st.session_state['tab'] = item

    st.write("---")

    # --- VIP 內容顯示區 ---
    curr = st.session_state['tab']
    
    if curr != "主目錄":
        if st.session_state['logged_in']:
            st.subheader(f"📍 當前位置：{curr}")
            
            # --- 實作：五. 懶人穩勝法 (新功能) ---
            if "五." in curr:
                st.markdown("### 🐢 80% 穩勝技法：大週期判斷")
                st.info("核心：周線 + 均線 + 爆量。先看指數方向，再決定個股多空。")
                
                # 分段診斷
                st.markdown("#### 1️⃣ 周線級別診斷 (20MA/60MA)")
                col_a, col_b = st.columns(2)
                with col_a:
                    under_20ma = st.checkbox("K棒是否在周線 20MA 之下？")
                with col_b:
                    above_all = st.checkbox("K棒是否同時站穩周線 20MA 與 60MA？")
                
                if under_20ma:
                    st.error("🚨 **空頭警報**：下跌至周線 20MA 之下，空頭機率極高，建議先賣出。")
                if above_all:
                    st.success("🚀 **多頭確認**：站穩 20MA 且不跌破 60MA，80% 認定站回多頭波段。")

                st.divider()
                st.markdown("#### 2️⃣ 月線級別策略 (KDJ 指標)")
                st.write("請觀察 **投資先生 KDJ 月線 ETF 交叉線**：")
                kdj_val = st.radio("當前 KDJ 交叉狀態：", ["20 下方往上交叉 (金叉)", "80 上方往下交叉 (死叉)", "區間震盪中"])
                
                if "20 下方" in kdj_val:
                    st.success("💰 **絕佳進場點**：月線級別低檔金叉，建議積極做多。")
                elif "80 上方" in kdj_val:
                    st.warning("📉 **出場警訊**：月線級別高檔死叉，準備獲利了結，撤離戰場。")

            # --- 實作：四. 均線做法 ---
            elif "四." in curr:
                timeframe = st.selectbox("請選擇觀察時框：", ["1分鐘線", "5分鐘線", "15~60分鐘線", "4小時線", "周線"])
                if "1分鐘" in timeframe:
                    st.warning("5MA 爆量判斷：起漲點為跌破漲回；起跌點為突破跌破。")
                elif "5分鐘" in timeframe:
                    st.write("5分線突破 200MA 做多，跌回賣出。")
                elif "60分鐘" in timeframe:
                    st.error("60MA 為中期轉折線：跌破先逃，漲回先買。")
                elif "周線" in timeframe:
                    st.error("💀 周線級別盤整跌破 = 股災。")

            # --- 實作：一/二/七 模組 (保留之前功能) ---
            elif "一." in curr:
                state = st.radio("形態：", ["斜的盤整", "橫的盤整"])
                if st.toggle("守住 1H 20MA?"): st.success("多頭慣性維持")
            elif "二." in curr or "三." in curr:
                hp = st.number_input("箱頂", value=100.0)
                lp = st.number_input("箱底", value=80.0)
                st.metric("🚀 目標價", f"{hp + (hp-lp):.2f}")
            elif "七." in curr:
                total = st.number_input("總資產(萬)", value=100.0)
                st.write(f"60% 高股息: {total*0.6:.1f}萬")
            
            else:
                st.info(f"「{curr}」內容建置中...")
        else:
            st.warning("🔒 此為 VIP 專屬內容，請先登入 (1234)。")

    st.write("---")
    st.caption("© 2026 股票心法 VIP | 核心技術支援：比爾蓋茲")
