# モック作成プロンプト

あなたは経験豊富なPython開発者です。`ideation/step3_prfaq.md` のPR/FAQを基に、動作するモックアプリケーションを作成してください。

## 重要な制約事項

**必ず以下を守ってください：**

1. **Python 3.11を使用** - 他のバージョンは使用しない
2. **出力先は`mock/`ディレクトリ** - `mock_app/`や他の名前は使用しない
3. **`strands-agents`パッケージを使用** - `strands`ではなく`strands-agents`
4. **技術スタックはユーザーに選択させる** - 勝手に決めない

## 技術スタック選択

**重要**: 必ずユーザーに以下の選択肢を提示し、選択してもらってください：

### オプション1: Streamlit + Strands Agent（推奨）
- 最速で実装可能
- インタラクティブなUIが簡単
- 複数ページの構成が容易
- Strands Agentで生成AI処理を実装
- 90分のアイディアソンに最適

### オプション2: FastAPI + HTML + Strands Agent
- デザインの自由度が高い
- 柔軟なUI設計が可能
- Strands Agentで生成AI処理を実装
- コード量が多い

## 要件

### 必須機能
1. ランディングページ: サービス概要、主要機能の説明
2. メイン機能ページ: PR/FAQで説明した主要機能の体験UI
3. Strands Agent処理: 生成AIを活用した処理（前回ハンズオンの知識を活用）
4. 結果表示ページ: 処理結果の表示

### 技術要件
- **Python 3.11** (必須)
- Strands Agent SDK (`strands-agents`)
- Amazon Bedrock (`.env`で設定)
- ローカルで動作
- uv + venv環境で実行
- 必要最小限の依存関係
- **出力先**: `mock/` ディレクトリ (必須)

### Strands Agent実装

前回ハンズオンで学んだStrands Agentを活用してください：

```python
from strands import Agent, tool
from dotenv import load_dotenv
import os

# .envから環境変数を読み込み
load_dotenv()

# Agentの作成
agent = Agent(
    model=os.getenv('AWS_BEDROCK_MODEL_ID'),
    system_prompt="あなたは...",
    tools=[...]  # 必要に応じてカスタムツールを定義
)

# 処理の実行
response = agent(user_input)
```

**参考**: 前回ハンズオンのサンプルコード
- `temp/ai-hackathon-2025-hands-on/workshop/examples/01_basic_agent.py`
- `temp/ai-hackathon-2025-hands-on/workshop/examples/02_custom_tools.py`

### 制約
- AWSデプロイ不要
- npm不要
- ローカルで完結
- ポン出しレベルでOK
- Strands Agentの処理は簡易的でOK（複雑なツールは不要）

## 実装手順

1. **ユーザーに技術スタックを選択させる**（StreamlitまたはFastAPI）
2. **`mock/`ディレクトリを作成**（他の名前は使わない）
3. PR/FAQの分析（サービス名、主要機能、UI要素を抽出）
4. **Python 3.11用のコードを生成**
5. **Strands Agent (`strands-agents`)を使った処理部分の実装**
6. UIコードの生成（シンプルで読みやすく）
7. **requirements.txtに`strands-agents`を含める**
8. README.mdの作成（.env設定手順を含む）

## README.mdに含める内容

```markdown
# [サービス名] モック

## 前提

- Python 3.11

## 事前準備

1. `.env`ファイルの作成
   ```bash
   cp ../.env.sample .env
   ```

2. `.env`ファイルを編集し、Bedrock APIキーを設定
   ```
   AWS_BEARER_TOKEN_BEDROCK=your-api-key-here
   AWS_REGION=ap-northeast-1
   AWS_BEDROCK_MODEL_ID=global.anthropic.claude-haiku-4-5-20251001-v1:0
   ```

## 起動方法

1. 仮想環境の作成と有効化
   ```bash
   uv venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

2. 依存関係のインストール
   ```bash
   uv pip install -r requirements.txt
   ```

3. アプリの起動
   ```bash
   streamlit run app.py  # Streamlitの場合
   python app.py         # FastAPIの場合
   ```

4. ブラウザで開く
   - Streamlit: http://localhost:8501
   - FastAPI: http://localhost:8000
```

## 注意事項
- 完璧を求めない
- デザインは最小限
- エラーハンドリングは簡易的
- Strands Agentの処理は簡易的でOK
- 前回ハンズオンのサンプルコードを参考にする

## requirements.txtに含めるべきパッケージ

```
streamlit  # Streamlitの場合
fastapi    # FastAPIの場合
uvicorn    # FastAPIの場合
strands-agents  # Strands Agent SDK (必須)
python-dotenv
```
