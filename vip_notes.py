import streamlit as st
import yfinance as yf
import pandas as pd

# 1. 頁面配置
st.set_page_config(page_title="股票心法 VIP 5.0", layout="wide", page_icon="📈")

# 2. 初始化 Session 狀態
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "九大心法"

# --- 側邊欄 ---
with st.sidebar:
    st.title("🔐 VIP 系統")
    if not st.session_state['logged_in']:
        u = st.text_input("帳號", key="u")
        p = st.text_input("密碼", type="password", key="p")
        if st.button("確認進入系統", use_container_width=True):
            if u == "1234" and p == "1234":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("密碼錯誤")
    else:
        st.success("✅ VIP 已登入")
        if st.button("📖 完整九大心法", use_container_width=True): st.session_state['tab'] = "九大心法"
        if st.button("🛡️ 12條保命準則", use_container_width=True): st.session_state['tab'] = "保命準則"
        if st.button("🚀 自動化診斷", use_container_width=True): st.session_state['tab'] = "自動化診斷"
        st.divider()
        if st.button("安全登出", use_container_width=True):
            st.session_state['logged_in'] = False
            st.rerun()

# --- 主畫面內容 ---
if not st.session_state['logged_in']:
    st.info("🔒 歡迎來到 VIP 專屬系統，請由左側登入。")
else:
    if st.session_state['tab'] == "九大心法":
        st.header("📖 股票心法操作順序 (100% 完整還原)")
        
        # 一. 畫趨勢線
        with st.expander("一. 畫趨勢線", expanded=True):
            st.write("### 趨勢線 - 找方向與最低價 (建議年線)")
            st.write("1. 用年線畫可以找到歷來平均最高點跟最低點，方向較準。")
            st.write("2. 容易看到爆量下影線的位置。")
            st.write("3. 沒有爆量也適合找月線裸K低點。")
            st.write("4. 1分線趨勢線波動值約 50 點。K棒在 20MA 爆量上漲進場，爆量跌破 5MA 出場。")
            st.write("5. 1分線 K 站在 20MA 下方，站上又跌破為下跌趨勢，需等爆量站上 20MA。")
            st.write("6. 爆量低點可畫趨勢線，跌破先走。")
            st.write("7. 短線 15 分線，K 在 20MA 以下進場，算 2 波下跌。")
            st.write("8. 5日線上多頭，5日線下空頭。")
            st.write("9. 先以 1 小時線以上畫趨勢，再用短線找進場。")
            st.write("10. 1 小時 20MA 突破/跌破，畫箱型確認。")

        # 二. 畫箱型
        with st.expander("二. 畫箱型+波段+壓力支撐線"):
            st.write("1. 爆量下影線往上畫至前高整理區箭頭為一波，通常漲 2-3 波，運氣好 5 波。")
            st.write("2. 畫完一波即為正方形箱型，需手動畫出。")
            st.write("3. 最高/最低點即為壓力與支撐。")
            st.write("4. 箱型突破需站穩 20MA 才是新波段；跌破則反之。")

        # 三. 箱型突破找點
        with st.expander("三. 用箱形突破找加碼與出場"):
            st.write("### A 部分")
            st.write("1. 箱型剛突破可加碼，但要站上 20MA 畫趨勢線。")
            st.write("2. 趨勢線跌破 20MA 出場。")
            st.write("3. 箱型突破/跌破需與 20MA/200MA 配合。")
            st.write("4. 持續跌破 60MA 轉為下跌箱型。")
            st.write("5. 畫箭頭可知下一波低點在哪。")
            st.write("### B 部分 (中間線法則)")
            st.write("1. 算箱型頭部到底價差 (如 100-90=10)，除以 2 為中間值 (95塊)。")
            st.write("2. 觀察哪條均線跌破中間線即出場。")
            st.write("3. 箱型底部買兩張 (長/短分開)。")
            st.write("4. 箱內小盤整也可畫波段箭頭找停損利。")
            st.write("5. 15分線一波 400 點，下跌也可能 400 點。")

        # 四. 均線做法
        with st.expander("四. 均線做法"):
            st.write("1. 1小時跌破 60MA 逃，漲回買。")
            st.write("2. 1小時 20MA 是箱型確認位置。站上通常是多頭。")
            st.write("3. 5分線突破 200MA 做多，跌回賣。")
            st.write("4. 4小時 20MA 破，往 60/200MA 尋找支撐。")
            st.write("5. 1分線 5MA 下爆量跌破又漲回是起漲；上爆量突破又跌破是起跌。")
            st.write("6. 20MA 糾結即盤整。周線級別盤整跌破是股災。")

        # 五、六. 懶人與裸K
        with st.expander("五. 懶人穩勝法 & 六. 單純找裸K"):
            st.write("**懶人法：** 下跌至周線 20MA 下賣出；站上周線 20MA/60MA 為多頭。KDJ 月線 20 以下交叉多，80 下交叉空。")
            st.write("**裸K：** 找底部長久短 K 盤整 + 爆量上漲 (翻倍機會)。找周、月、年線大 K 棒。")

        # 七、八. 資金與支撐
        with st.expander("七. 資金分配法 & 八. 精準支撐壓力"):
            st.write("**資金：** 60% 高股息 ETF、30% 波動型、10% 短線。獲利 20% 出 10%，跌 20% 進 20%。看 K 棒不盯數字。")
            st.write("**支撐壓力：** 下跌趨勢起始頭部為壓力；上升趨勢起始底部為支撐。")

    elif st.session_state['tab'] == "保命準則":
        st.header("🚨 九. 緊急下跌狀況注意提醒")
        st.warning("12 條保命準則：")
        st.write("1. 加碼看 1/5 分線 200MA 站穩沒。")
        st.write("2. 期貨結算日常持續下跌。")
        st.write("3. 跌破爆量 K 最低點必出場。")
        st.write("4. 早盤 15 分最大量 K 跌破。")
        st.write("5. 5分線 200MA 下午跌破先走。")
        st.write("6. 1小時 60MA、周線 20MA 跌破皆先走。")
        st.write("7. 假突破進場被跌回馬上下，真突破再買回。")
        st.write("8. 箱型破底翻要趕快買回，否則少賺一整箱。")
        st.info("開盤前勿買，勿買最高點。")

    elif st.session_state['tab'] == "自動化診斷":
        st.header("🚀 數據診斷")
        symbol = st.text_input("輸入代碼 (2330.TW)", "2330.TW")
        if st.button("執行"):
            df = yf.download(symbol, period="5y")
            st.line_chart(df['Close'])
