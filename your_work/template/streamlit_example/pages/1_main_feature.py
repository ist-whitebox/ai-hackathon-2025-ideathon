import streamlit as st
import time

st.title("メイン機能")
st.header("入力")
user_input = st.text_input("入力してください")
submit = st.button("実行")

if submit and user_input:
    st.header("結果")
    with st.spinner("処理中..."):
        time.sleep(1)
    st.success("処理が完了しました！")
    st.write(f"入力: {user_input}")
    st.write(f"結果: [ダミーの処理結果]")
