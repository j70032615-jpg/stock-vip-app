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
        "五. 懶人高勝法", 
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
            
            # --- 實作：四. 均線做法 (心法精華) ---
            if "四." in curr:
                st.info("💡 均線核心：均線代表內心的波動值。請根據股票最近的慣性，觀察 K 棒貼著哪一條線走。")
                
                timeframe = st.selectbox("請選擇您目前觀察的時框：", 
                    ["1分鐘線 (極短線)", "5分鐘線 (期貨)", "15/30/60分鐘線 (波段轉折)", "4小時線 (中期趨勢)", "周線 (大級別)"])

                if "1分鐘" in timeframe:
                    st.markdown("#### ⚡ 極短線 1分線戰法")
                    st.warning("⚠️ 5MA 爆量判斷：")
                    st.write("- **起漲點**：K 棒在 5MA 下爆量跌破又漲回。")
                    st.write("- **起跌點**：K 棒在 5MA 上爆量突破又跌破。")
                    st.caption("註：若沒明顯爆量，請拉長至 5 或 15 分線觀察。")

                elif "5分鐘" in timeframe:
                    st.markdown("#### 📉 期貨 5分線戰法")
                    st.write("- **做多訊號**：K 棒從底部突破 200MA。")
                    st.write("- **出場訊號**：等下次 K 棒跌回 200MA 時賣出。")

                elif "60分鐘" in timeframe or "15/30" in timeframe:
                    st.markdown("#### ⏳ 波段轉折 (15~60分線)")
                    st.error("🚨 60MA 轉折線：跌破先逃，漲回先買。通常不會跌破 200MA。")
                    st.success("📦 20MA 箱型確認：站上通常為多頭，可看 15分線 60MA 擇機進場。")
                    st.warning("🧐 盤整警訊：若 30/60分線與 200MA 距離極接近且來回糾結，需留意箱型突破。")

                elif "4小時" in timeframe:
                    st.markdown("#### 🏛️ 中期趨勢 (4H線)")
                    st.write("- **風險警示**：跌破 20MA，股價可能向下尋求 60MA 或 200MA 支撐。")

                elif "周線" in timeframe:
                    st.markdown("#### 🌋 大級別周線")
                    st.error("💀 盤整跌破：周線等級盤整跌破即為「股災」，必須全面撤退。")

            # --- 實作：一. 趨勢線 ---
            elif "一." in curr:
                st.markdown("### 📐 趨勢與盤整形態診斷")
                st.info("心法：趨勢線走完斜的盤整後，會切換成橫的盤整，再做一次斜的。通常不會跌破 1小時 20MA。")
                state = st.radio("當前形態觀察：", ["斜的盤整 (趨勢通道)", "橫的盤整 (箱型)"])
                ma_check = st.toggle("K棒是否守住 1小時 20MA？")
                if ma_check: st.success("✅ 多頭慣性維持。")
                else: st.error("❌ 慣性改變警告！")

            # --- 實作：二. 箱型 ---
            elif "二." in curr or "三." in curr:
                st.markdown("### 🎯 專業箱型目標價預測")
                c1, c2 = st.columns(2)
                hp = c1.number_input("壓力位 (箱頂)", value=100.0)
                lp = c2.number_input("支撐位 (箱底)", value=80.0)
                box_h = hp - lp
                st.metric("🛡️ 中軸守備線", f"{lp + (box_h / 2):.2f}")
                st.metric("🚀 突破目標價", f"{hp + box_h:.2f}")

            # --- 實作：七. 資金分配 ---
            elif "七." in curr:
                total = st.number_input("總資產 (萬元)", value=100.0)
                st.write(f"📊 60% 高股息: {total*0.6:.1f} 萬")
                st.write(f"📊 30% 波動型: {total*0.3:.1f} 萬")
                st.write(f"📊 10% 短線個股: {total*0.1:.1f} 萬")
            
            else:
                st.info(f"「{curr}」的心法內容數位化建置中...")
        else:
            st.warning("🔒 此為 VIP 專屬內容，請先登入 (1234)。")

    st.write("---")
    st.caption("© 2026 股票心法 VIP | 核心開發：比爾蓋茲")
