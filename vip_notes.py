import streamlit as st

# 1. 頁面配置
st.set_page_config(page_title="股票心法 VIP 系統", layout="wide")

# 2. 初始化 Session 狀態
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "主目錄"

# --- 側邊欄：登入與權限 ---
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

    menu = ["一. 趨勢線與盤整切換", "二. 箱型波段預測", "七. 資金分配法", "九. 緊急提醒"]
    
    for i, item in enumerate(menu):
        if st.button(item, key=f"menu_{i}", use_container_width=True):
            st.session_state['tab'] = item

    st.write("---")

    # --- VIP 內容顯示區 ---
    curr = st.session_state['tab']
    
    if curr != "主目錄":
        if st.session_state['logged_in']:
            st.subheader(f"📍 當前模組：{curr}")
            
            # --- 心法一：趨勢線與盤整切換 ---
            if "趨勢線" in curr:
                st.markdown("### 📐 形態診斷：階梯式趨勢切換")
                st.info("心法：趨勢線走完斜的盤整後，會切換成橫的盤整，再做一次斜的。")
                
                state = st.radio("當前形態觀察：", ["斜的盤整 (趨勢通道)", "橫的盤整 (箱型)"])
                
                if state == "斜的盤整 (趨勢通道)":
                    st.success("🔎 **診斷：趨勢延伸中**。接下來預期會進入橫盤。")
                else:
                    st.warning("🔎 **診斷：進入橫盤蓄勢**。接下來預期將再次啟動斜盤。")
                
                st.divider()
                st.markdown("#### 🛡️ 慣性守備指標")
                ma_check = st.toggle("K棒是否守住 1小時 20MA？")
                if ma_check:
                    st.success("✅ **維持原盤整波段**：多頭慣性未改變。")
                else:
                    st.error("❌ **慣性改變警告**：跌破 1H 20MA，注意型態反轉！")

            # --- 心法二：箱型波段預測 ---
            elif "箱型" in curr:
                st.markdown("### 🎯 專業箱型目標預測")
                c1, c2 = st.columns(2)
                hp = c1.number_input("最高點 (100)", value=100.0)
                lp = c2.number_input("最低點 (80)", value=80.0)
                box_h = hp - lp
                mid_p = lp + (box_h / 2)
                
                res1, res2, res3 = st.columns(3)
                res1.metric("箱型高度", f"{box_h:.2f}")
                res2.metric("🛡️ 中軸守備", f"{mid_p:.2f}")
                res3.metric("🚀 第二波目標", f"{hp + box_h:.2f}")
                st.success(f"💡 建議進場位：{mid_p} 以下，波動小且勝率高。")

            # --- 心法七：資金分配法 ---
            elif "資金" in curr:
                st.markdown("### 💰 6-3-1 專業資產配置")
                total = st.number_input("請輸入總資產 (萬元)", value=100.0, step=10.0)
                st.write(f"📊 **60% 高股息 ETF:** {total*0.6:.1f} 萬")
                st.write(f"📊 **30% 波動型 ETF:** {total*0.3:.1f} 萬")
                st.write(f"📊 **10% 短線個股:** {total*0.1:.1f} 萬")
            
            else:
                st.info("內容建置中...")
        else:
            st.warning("🔒 此為 VIP 會員專屬內容，請先從左側登入 (1234)。")

    st.write("---")
    st.caption("© 2026 股票心法 VIP | 核心開發：比爾蓋茲")
