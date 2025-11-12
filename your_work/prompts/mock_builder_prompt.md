# モック作成プロンプト

あなたは経験豊富なPython開発者です。`ideation/step3_prfaq.md` のPR/FAQを基に、動作するモックアプリケーションを作成してください。

## 技術スタック選択

まず、ユーザーに選択させてください：

### オプション1: Streamlit（推奨）
- 最速で実装可能
- インタラクティブなUIが簡単
- 複数ページの構成が容易
- 90分のアイディアソンに最適

### オプション2: FastAPI + HTML
- デザインの自由度が高い
- 柔軟なUI設計が可能
- コード量が多い

## 要件

### 必須機能
1. ランディングページ: サービス概要、主要機能の説明
2. メイン機能ページ: PR/FAQで説明した主要機能の体験UI
3. 結果表示ページ: 処理結果の表示（ダミーデータでOK）

### 技術要件
- Python 3.11+
- ローカルで動作
- uv + venv環境で実行
- 必要最小限の依存関係

### 制約
- AWSデプロイ不要
- npm不要
- ローカルで完結
- ポン出しレベルでOK
- ダミーデータ・モック処理でOK

## 実装手順

1. 技術スタックの選択（StreamlitまたはFastAPI+HTML）
2. PR/FAQの分析（サービス名、主要機能、UI要素を抽出）
3. ディレクトリ構成の作成
4. コード生成（シンプルで読みやすく）
5. README.mdの作成

## README.mdに含める内容

```markdown
# [サービス名] モック

## 起動方法

1. 仮想環境の作成と有効化
   uv venv
   source .venv/bin/activate

2. 依存関係のインストール
   uv pip install -r requirements.txt

3. アプリの起動
   streamlit run app.py  # Streamlitの場合
   python app.py         # FastAPIの場合

4. ブラウザで開く
   Streamlit: http://localhost:8501
   FastAPI: http://localhost:8000
```

## 注意事項
- 完璧を求めない
- デザインは最小限
- エラーハンドリングは簡易的
- データは全てダミー
