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
        "一. 畫趨勢線確認位置", "二. 畫箱型 + 波段 + 壓力支撐線", 
        "三. 用箱形突破找加碼點跟出場點", "四. 均線做法", 
        "五. 懶人穩勝法", "六. 單純找裸K選股", 
        "七. 資金分配法", "八. 精準支撐壓力", 
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
            
            # --- 實作：八. 精準支撐壓力 (最新形態診斷) ---
            if "八." in curr:
                st.markdown("### 📐 形態畫線：從轉折找壓力與支撐")
                st.info("心法：必須有形態出現（V、N、M、A）才能畫線。TradingView 腳本僅供參考，心法才是核心。")
                
                pattern = st.selectbox("請選擇您目前看到的形態：", 
                    ["V型/N型 (轉折向上)", "M頭/A頭 (轉折向下)", "盤整跌/盤整翻 (方向切換)"])
                
                if "V型/N型" in pattern:
                    st.success("✅ **支撐確認**：請將支撐線畫在 V 型的最底端點，或 N 型的第二個低點。")
                    st.write("💡 策略：回測此支撐線不破，是極佳的介入點。")
                elif "M頭/A頭" in pattern:
                    st.error("🚨 **壓力確認**：請將壓力線畫在 M 頭的兩個高點連線，或 A 頭的最頂點。")
                    st.write("💡 策略：若價格無法有效突破此壓力線，波段獲利應先行了結。")
                else:
                    st.warning("🧐 **方向不明**：盤整中需尋找箱型頂與箱型底，等待突破/跌破。")

                st.divider()
                st.markdown("#### 🛠️ 手動計算壓力位")
                p_high = st.number_input("輸入前波高點 (壓力參考)", value=100.0)
                p_low = st.number_input("輸入前波低點 (支撐參考)", value=80.0)
                st.write(f"📊 目前波段空間為： **{p_high - p_low:.2f}**")
                st.caption("註：形態的極點就是最精準的線，不需要依賴過多指標。")

            # --- 實作：其餘模組 (保持原邏輯) ---
            elif "六." in curr:
                st.markdown("### 🕯️ 裸 K 操盤")
                st.write("尋找底部短 K 吃貨痕跡，等待長線跌轉漲大 K。")
            elif "五." in curr:
                st.markdown("### 🐢 80% 穩勝法")
                st.write("觀察周線 20MA/60MA 與月線 KDJ 金叉/死叉。")
            elif "四." in curr:
                st.write("均線慣性診斷模組。")
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
