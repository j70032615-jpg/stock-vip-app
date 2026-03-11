import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

# 1. 頁面配置
st.set_page_config(page_title="股票心法 VIP 3.5 終極版", layout="wide", page_icon="📈")

# 2. 初始化 Session 狀態
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'tab' not in st.session_state:
    st.session_state['tab'] = "九大心法"

# --- 側邊欄 ---
with st.sidebar:
    st.title("🔐 VIP 會員系統")
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
        st.header("📖 股票心法操作順序 (完整版)")
        
        with st.expander("一、畫趨勢線", expanded=True):
            st.write("""
            **趨勢線-可以找到當前股票持續走的大方向跟最低價位 建議直接用年線去畫**
            1. 用年線畫可以找到歷來平均最高點跟最低點 方向也會比較準
            2. 也比較容易看到爆量下影線的位置在哪 
            3. 沒有爆量 也適合找月線裸K低點
            4. 1分線的趨勢線會有波動值可以找50點左右的波動來做. K棒在20MA爆量上漲的進場.K棒爆量跌破5MA出場
            5. 1分線K棒在20MA下方 站上20MA又跌破 為走下跌趨勢線 需等待爆量站上20MA
            6. 爆量的低點可畫趨勢線 跌破先走****(突然大跌 止跌也可畫)
            7. 短線走15分線 K棒在20MA以下再進場 可算2波下跌 趨勢線上漲的情況
            8. 最簡單畫趨勢線的方式是判斷K棒 持續站在5日線上方畫為多頭 持續跌破為空頭
            9. 短線盡量先以1小時線以上去畫趨勢線 才用更短的時間找進場位置
            10. 1小時20日線突破或跌破 要畫箱型確認跌破要跑突破要追
            """)

        with st.expander("二、畫箱型+波段+壓力支撐線"):
            st.write("""
            1. 從爆量下影線的K棒位置 往上畫到一個接近前波高點的整理區的箭頭線為1波，通常都會漲2波-3波運氣好有5波
            2. 畫完一波也剛好成為一個正方形箱型.需動手將正方形畫起來
            3. 而最低跟最高點就分別是壓力與支撐線.有免費指標可用 也可自己動手畫起來
            4. 箱型被突破K棒要持續站在20MA上方 才是新波段的箱型.如箱形被跌破K棒要持續站在20MA下方 是新的下跌波段箱型
            **止跌反彈 或上漲回跌 都可以準備畫箱型
            """)

        with st.expander("三、用箱形突破找加碼點跟出場點"):
            st.write("""
            **箱型+趨勢線+均線(最好的位置就是箱型底部的起漲箱型)**
            **A.**
            1. 箱型剛突破後 可以加碼 但要站上20MA均線 來畫上趨勢線
            2. 趨勢線跌破20MA時就出場以此類推
            3. 箱型突破K棒要持續站在20MA上方
            4. 箱形跌破K棒要持續站在20MA下方或200MA
            5. 持續跌破60MA要小心轉為下跌箱型
            6. 畫完完整箱型 可以畫箭頭 最高到最低為一波段 可以畫第二個箭頭可知道下一波低點在哪
            **B. 在箱型中間畫一條線**
            1. 畫好箱型，算箱型頭部到底有多少價差 假設頭部100塊 底部90塊，取中間值(100-90)/2=5，也就是95塊劃一條線
            2. 每切換時間線可觀察到是哪條均線跌破中間線 跌破要出場
            3. 可在廂型底部買2張股票一張放長期一張做短期，畫上趨勢線碰到底部買 碰到頭部賣.切記配合均線跟中間線.
            4. 箱型裡面出現的小盤整形態也可以畫一個波段箭頭 當突破或跌破時 即可劃出停損停利點
            """)

        with st.expander("四、均線做法"):
            st.write("""
            1. 1小時線跌破60MA先逃. 漲回60MA先買 通常不會跌破200MA.所以60MA是一個中期的轉折線.
            2. 1小時20MA是箱型確認的位置.盤整是準備換下一個箱型跟換一下一個趨勢線的準備.
            3. 極短線期貨5分線的K棒從底部突破200日線後 可做多 等下次K棒跌回200日線在賣
            4. 4小時的20日均線被跌破就可能往60日或200日均線下跌
            5. 極短線1分線K棒在5MA下爆量跌破又漲回是起漲點
            6. 極短線1分線K棒在5MA上爆量突破又跌破當根K棒是起跌點
            7. 20MA K棒一直在來回均線糾結的話 就是盤整. 周線級別盤整跌破是股災
            8. 30分或1小時線200MA跌破又突破的距離 一直都很接近的話 也是盤整要非常留意箱型突破跌破
            """)

        with st.expander("五、懶人穩勝法 & 六、裸K
