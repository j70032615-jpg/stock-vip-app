import streamlit as st

def show_box_theory_tool():
    st.subheader("🎯 箱型波段與目標價預測器")
    st.info("根據您的心法：找出箱型頂部與底部，預測下一波噴發目標。")

    # 1. 輸入參數區
    col_input1, col_input2 = st.columns(2)
    with col_input1:
        high_price = st.number_input("請輸入箱型最高點 (壓力線)", value=100.0, step=0.1)
    with col_input2:
        low_price = st.number_input("請輸入箱型最低點 (支撐線)", value=80.0, step=0.1)

    # 2. 核心邏輯運算 (這部分會員看不到公式)
    box_height = high_price - low_price  # 箱型高度
    mid_point = low_price + (box_height / 2)  # 箱型中位線
    target_1 = high_price + box_height  # 第二波目標
    target_2 = target_1 + box_height    # 第三波目標

    st.write("---")

    # 3. 結果呈現區 (視覺化美化)
    res_col1, res_col2, res_col3 = st.columns(3)
    
    with res_col1:
        st.metric("📦 箱型高度", f"{box_height:.2f}")
    with res_col2:
        st.metric("🛡️ 強弱中位線", f"{mid_point:.2f}", help="股價在中位線以下進場，勝率較高且波動較小")
    with res_col3:
        st.success(f"🚀 突破目標：{target_1:.2f}")

    # 4. 專業警示與建議
    st.markdown(f"""
    ### 📊 VIP 實戰導航紀錄：
    * **箱型區間**：`{low_price}` ~ `{high_price}`
    * **進場策略**：建議在 **{mid_point}** 以下尋找爆量起漲點。
    * **目標預測**：
        - 第一波波段：`{high_price}` (已達成)
        - 第二波預測：**{target_1}**
        - 第三波預測：**{target_2}**
    * **停損提醒**：若 K 棒重新跌破 **{mid_point}** 需高度戒備，跌破 **{low_price}** 則箱型失敗。
    """)

    # 這裡可以預留一個圖表空間，未來我們串接即時 K 線
    st.caption("註：本計算根據『箱型+波段+壓力支撐線』心法自動生成。")

# 在主程式目錄中調用
# if st.button("三. 用箱形突破找加碼點跟出場點"):
#     show_box_theory_tool()
