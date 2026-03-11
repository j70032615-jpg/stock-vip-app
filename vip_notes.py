# 實作：趨勢線診斷 (心法一)
            if "趨勢線" in curr:
                st.markdown("### 📐 趨勢與盤整形態診斷")
                state = st.radio("當前 K 棒走勢：", ["斜的盤整 (趨勢通道)", "橫的盤整 (箱型)"])
                
                if state == "斜的盤整 (趨勢通道)":
                    st.success("🔎 診斷：趨勢延伸中")
                    st.write("依據心法：趨勢線走完斜的後，會切換成橫的盤整。")
                else:
                    st.warning("🔎 診斷：進入橫盤蓄勢")
                    st.write("依據心法：橫盤完畢後，預期將再次啟動斜的趨勢。")
                
                st.divider()
                st.markdown("#### 🛡️ 核心守備：1小時 20MA")
                ma_status = st.toggle("K 棒是否站穩 1H 20MA？")
                
                if ma_status:
                    st.success("✅ 多頭慣性維持：建議維持原盤整波段趨勢操作。")
                else:
                    st.error("❌ 慣性改變警告：跌破 1H 20MA，需注意盤整型態是否反轉！")
