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
            
            # --- 實作：六. 單純找裸 K 選股 (最新整合) ---
            if "六." in curr:
                st.markdown("### 🕯️ 裸 K 操盤：找尋主力吃貨痕跡")
                st.info("核心心法：找尋底部盤整的短 K 棒（主力吃貨），並等待爆量上漲的大 K 棒（跌轉漲）。")
                
                # 診斷器
                st.markdown("#### 🔍 形態診斷器")
                k_type = st.radio("觀察當前 K 棒型態：", 
                    ["低檔短 K 橫盤 (默默吃貨中)", "爆量拉升長 K (起漲訊號)", "高檔大 K (注意風險)"])
                
                if "短 K" in k_type:
                    st.success("💎 **潛力股觀察**：吃貨越久，爆量後漲幅空間越大（有機會漲 100%）。")
                    st.write("💡 建議：此時應保持耐心，觀察量能是否開始放大。")
                elif "爆量" in k_type:
                    st.warning("🚀 **起漲確認**：這可能是跌轉漲的轉折點！")
                    st.write("💡 操作：檢查是否從周、月、半年線或年線級別啟動。")

                st.divider()
                st.markdown("#### 📅 長線級別確認")
                time_level = st.multiselect("請確認目前在哪個長線級別出現『跌轉漲』大 K 棒：", 
                    ["周線", "月線", "半年線", "年線"])
                
                if time_level:
                    st.success(f"✅ 已在 {', '.join(time_level)} 級別確認跌轉漲。這屬於高勝率裸 K 型態！")

            # --- 實作：五. 懶人穩勝法 ---
            elif "五." in curr:
                st.markdown("### 🐢 80% 穩勝技法")
                col_a, col_b = st.columns(2)
                with col_a: u20 = st.checkbox("K棒在周線 20MA 之下？")
                with col_b: a60 = st.checkbox("站穩周 20MA 與 60MA？")
                if u20: st.error("🚨 空頭機率高，先賣出。")
                if a60: st.success("🚀 多頭確認，80% 穩勝。")
                st.divider()
                kdj = st.radio("月線 KDJ：", ["20 下方金叉 (進場)", "80 上方死叉 (準備出場)"])
                if "20" in kdj: st.success("💰 絕佳進場位。")

            # --- 實作：其餘模組 (保留之前功能) ---
            elif "四." in curr:
                st.write("均線慣性診斷模組（1分/5分/1H/周線）。")
            elif "一." in curr:
                st.write("趨勢與盤整形態切換診斷（斜盤/橫盤）。")
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
