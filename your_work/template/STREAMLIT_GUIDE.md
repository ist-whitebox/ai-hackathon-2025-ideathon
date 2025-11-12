# Streamlit モックアプリケーション ガイド

## 概要

このガイドでは、Streamlitを使用したモックアプリケーションの作成方法を説明します。

## 技術スタック

- Python 3.11+
- Streamlit 1.30+
- uv（パッケージマネージャー）

## プロジェクト構成

```
mock/
├── app.py                 # メインアプリケーション
├── pages/                 # 追加ページ
│   ├── 1_main_feature.py
│   └── 2_results.py
├── requirements.txt       # 依存関係
└── README.md             # 起動方法
```

## 基本的な実装

### app.py（メインページ）

```python
import streamlit as st

# ページ設定
st.set_page_config(
    page_title="サービス名",
    page_icon="🚀",
    layout="wide"
)

# ランディングページ
st.title("🚀 サービス名")
st.markdown("---")

# サービス概要
st.header("サービス概要")
st.write("ここにサービスの説明を記載します。")

# 主要機能
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

# CTA
st.markdown("---")
st.info("👈 サイドバーから各機能を体験できます")
```

### pages/1_main_feature.py（機能ページ）

```python
import streamlit as st
import time

st.title("メイン機能")

# 入力フォーム
st.header("入力")
user_input = st.text_input("入力してください")
submit = st.button("実行")

# 処理と結果表示
if submit and user_input:
    st.header("結果")
    
    # ダミー処理
    with st.spinner("処理中..."):
        time.sleep(1)
    
    # 結果表示
    st.success("処理が完了しました！")
    st.write(f"入力: {user_input}")
    st.write(f"結果: [ダミーの処理結果]")
```

## 起動方法

### 1. 仮想環境の作成

```bash
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 2. 依存関係のインストール

```bash
uv pip install -r requirements.txt
```

### 3. アプリケーションの起動

```bash
streamlit run app.py
```

### 4. ブラウザで開く

http://localhost:8501

## よく使うStreamlitコンポーネント

### 入力

```python
# テキスト入力
text = st.text_input("ラベル")

# テキストエリア
text = st.text_area("ラベル")

# 数値入力
number = st.number_input("ラベル", min_value=0, max_value=100)

# セレクトボックス
option = st.selectbox("選択してください", ["オプション1", "オプション2"])

# ボタン
if st.button("クリック"):
    st.write("ボタンがクリックされました")
```

### 表示

```python
# テキスト
st.write("テキスト")
st.markdown("**太字**")

# 見出し
st.title("タイトル")
st.header("ヘッダー")
st.subheader("サブヘッダー")

# メッセージ
st.success("成功メッセージ")
st.info("情報メッセージ")
st.warning("警告メッセージ")
st.error("エラーメッセージ")

# スピナー
with st.spinner("処理中..."):
    time.sleep(2)
```

### レイアウト

```python
# カラム
col1, col2, col3 = st.columns(3)
with col1:
    st.write("カラム1")

# タブ
tab1, tab2 = st.tabs(["タブ1", "タブ2"])
with tab1:
    st.write("タブ1の内容")

# エクスパンダー
with st.expander("詳細を表示"):
    st.write("詳細な内容")
```

## Tips

### ページ間でのデータ共有

```python
# セッションステートを使用
if 'data' not in st.session_state:
    st.session_state.data = []

# データの追加
st.session_state.data.append(new_data)

# データの取得
data = st.session_state.data
```

### ダミーデータの生成

```python
import random

# ランダムな結果を生成
result = random.choice(["成功", "失敗", "保留"])

# ダミーのリストデータ
dummy_data = [
    {"name": "項目1", "value": 100},
    {"name": "項目2", "value": 200},
]
```

## トラブルシューティング

### ポートが使用中

```bash
# 別のポートで起動
streamlit run app.py --server.port 8502
```

### キャッシュのクリア

```bash
streamlit cache clear
```

## 参考リンク

- [Streamlit公式ドキュメント](https://docs.streamlit.io/)
- [Streamlit API Reference](https://docs.streamlit.io/library/api-reference)
