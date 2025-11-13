# モックアプリケーション ガイド

## 概要

このガイドでは、アイディアソンで使用するモックアプリケーションの作成方法を説明します。

## 技術スタック選択

### オプション1: Streamlit（推奨）

**メリット:**
- 最速で実装可能
- インタラクティブなUIが簡単
- 複数ページの構成が容易
- 90分のアイディアソンに最適

**詳細:** [STREAMLIT_GUIDE.md](./STREAMLIT_GUIDE.md)

### オプション2: FastAPI + HTML

**メリット:**
- デザインの自由度が高い
- 柔軟なUI設計が可能
- REST API的な構成

**詳細:** [FASTAPI_GUIDE.md](./FASTAPI_GUIDE.md)

## 共通の起動手順

### 1. 仮想環境の作成

```bash
uv venv --python 3.11
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 2. 依存関係のインストール

```bash
uv pip install -r requirements.txt
```

### 3. アプリケーションの起動

**Streamlitの場合:**
```bash
streamlit run app.py
```
→ http://localhost:8501

**FastAPIの場合:**
```bash
python app.py
```
→ http://localhost:8000

## テンプレート

- `streamlit_example/` - Streamlitのサンプル
- `fastapi_example/` - FastAPIのサンプル

## 注意事項

- **ポン出しレベルでOK**: 完璧を求めない
- **デザインは最小限**: 機能の体験を優先
- **ローカルで完結**: AWSデプロイ不要
- **ダミーデータでOK**: 実際のAPIやDB不要

## トラブルシューティング

### ポートが使用中

**Streamlit:**
```bash
streamlit run app.py --server.port 8502
```

**FastAPI:**
```python
# app.py内で変更
uvicorn.run(app, host="0.0.0.0", port=8001)
```

### 依存関係のエラー

```bash
# 仮想環境を再作成
rm -rf .venv
uv venv --python 3.11
source .venv/bin/activate
uv pip install -r requirements.txt
```

## 参考リンク

- [Streamlit公式ドキュメント](https://docs.streamlit.io/)
- [FastAPI公式ドキュメント](https://fastapi.tiangolo.com/)
