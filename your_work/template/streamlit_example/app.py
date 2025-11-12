import streamlit as st

st.set_page_config(page_title="サービス名", page_icon="🚀", layout="wide")
st.title("🚀 サービス名")
st.markdown("---")
st.header("サービス概要")
st.write("ここにサービスの説明を記載します。")
st.header("主要機能")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("機能1")
    st.write("機能1の説明")
with col2:
    st.subheader("機能2")
    st.write("機能2の説明")
with col3:
    st.subheader("機能3")
    st.write("機能3の説明")
st.markdown("---")
st.info("👈 サイドバーから各機能を体験できます")
