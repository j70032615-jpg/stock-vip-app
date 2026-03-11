import streamlit as st

# 1. 基礎設定
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
            # 這裡幫你改好了，帳號 1234，密碼 1234
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

# --- 主畫面 ---
l_sp, m_col, r_sp = st.columns([1, 2, 1])

with m_col:
    st.markdown("<h1 style='text-align: center;'>📈 股票心法 VIP 系統</h1>", unsafe_allow_html=True)
    st.write("---")

    menu = ["一. 畫趨勢線", "二. 畫箱型波段", "三. 箱型突破加碼", "四. 均線做法", "五. 懶人高勝法", "六. 裸K選股", "七. 資金分配法", "八. 精準支撐壓力", "九. 緊急提醒"]

    for i, item in enumerate(menu):
        if st.button(item, key=f"m_{i}", use_container_width=True):
            st.session_state['tab'] = item

    st.write("---")

    # --- VIP 內容區 ---
    curr = st.session_state['tab']
    if curr != "主目錄":
        if st.session_state['logged_in']:
            st.subheader(f"📍 當前位置：{curr}")
            
            # 功能實作：箱型計算 (二、三)
            if "箱型" in curr:
                st.markdown("### 🎯 專業箱型目標價預測")
                c1, c2 = st.columns(2)
                hp = c1.number_input("箱型最高 (壓力)", value=100.0)
                lp = c2.number_input("箱型最低 (支撐)", value=80.0)
                box_h = hp - lp
                mid_p = lp + (box_h / 2)
                st.metric("🛡️ 中軸守備線", f"{mid_p:.2f}")
                st.metric("🚀 第二波目標", f"{hp + box_h:.2f}")
                st.info(f"💡 建議在 {mid_p} 以下尋找爆量起漲點，突破 {hp} 為加碼點。")

            # 功能實作：資金分配 (七)
            elif "資金" in curr:
                st.markdown("### 💰 6-3-1 資金比例管理")
                total = st.number_input("總可用資產 (萬元)", value=100.0, step=10.0)
                st.divider()
                st.write(f"📊 **60% 高股息 ETF:** {total*0.6:.1f} 萬")
                st.write(f"📊 **30% 波動型 ETF:** {total*0.3:.1f} 萬")
                st.write(f"📊 **10% 短線個股:** {total*0.1:.1f} 萬")
                st.success(f"建議短線個股每檔分配：{(total*0.1)/5:.2f} 萬 (以5檔計)")
            
            else:
                st.info(f"「{curr}」的心法細節與數位工具建置中...")
        else:
            st.warning("🔒 此功能內含核心公式，請先從左側登入 VIP 帳號。")
