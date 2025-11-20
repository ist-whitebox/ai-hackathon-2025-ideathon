# チェックリスト ✅

モックアプリケーションが完成したら、以下のチェックリストで確認してください。

---

## 🤖 Amazon Q Developer向け検証手順

**参考資料**: 
- [Strands Agents 公式ドキュメント](https://strandsagents.com/latest/documentation/docs/)
- [Amazon Bedrock Basic Usage](https://strandsagents.com/latest/user-guide/concepts/model-providers/amazon-bedrock/#basic-usage)
- [AWS Prescriptive Guidance - Strands Agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/strands-agents.html)

実行前に最新API仕様を確認してください。

**ユーザーから「チェックリストに沿ってチェックをしてください」と依頼されたら、以下を実行してください。**

### 重要な前提条件

- **カレントディレクトリ**: `mock/` ディレクトリで実行
- **仮想環境**: `mock/.venv/` が既に作成済みと想定
- **パッケージマネージャー**: `uv` を使用（`uv run python` でコマンド実行）
- **Python実行**: 仮想環境を明示的に有効化せず、`uv run` を使用

## Phase 0: 依存関係の確認

### 1. requirements.txtの確認

**必須確認項目：**
- [ ] `strands-agents`が含まれているか？
- [ ] 選択した技術スタック（`streamlit`または`fastapi`+`uvicorn`）が含まれているか？
- [ ] `python-dotenv`が含まれているか？

### 2. 仮想環境の確認

**前提**: 仮想環境は既に作成済み（`mock/.venv/`）

仮想環境が存在しない場合のみ作成：
```bash
cd mock/
uv venv --python 3.11
uv pip install -r requirements.txt
```

**確認項目：**
- [ ] 仮想環境が存在するか？（`mock/.venv/` ディレクトリ）
- [ ] パッケージがインストール済みか？

## Phase 1: Strands Agents記法の検証（最優先）

### 3. Strands APIの確認

**重要**: `uv run` を使用してPythonコマンドを実行

```bash
cd mock/
uv run python -c "import strands; print(dir(strands))"
```

### 4. Agent初期化パラメータの確認

```bash
uv run python -c "from strands import Agent; import inspect; sig = inspect.signature(Agent.__init__); print('主要パラメータ:'); params = ['model', 'system_prompt', 'tools', 'messages']; [print(f'  - {p}: {\"存在\" if p in sig.parameters else \"なし\"}') for p in params]"
```

**必須確認項目：**
- [ ] 使用可能なパラメータ名を確認
- [ ] `name`パラメータは存在するか？
- [ ] `instructions`パラメータは存在するか？
- [ ] `system_prompt`パラメータは存在するか？

### 5. Agent利用可能メソッドの確認

```bash
uv run python -c "from strands import Agent; methods = [m for m in dir(Agent) if not m.startswith('_')]; print('利用可能メソッド:'); [print(f'  - {m}') for m in ['invoke_async', 'stream_async', '__call__'] if m == '__call__' or m in methods]"
```

**必須確認項目：**
- [ ] `run()`メソッドは存在するか？
- [ ] `stream_async()`メソッドは存在するか？

### 6. AgentResult属性の確認（重要）

Agentの戻り値の正しい属性を確認：

```bash
cd mock/
uv run python -c "from strands import Agent; import os; from dotenv import load_dotenv; load_dotenv(); agent = Agent(model=os.getenv('AWS_BEDROCK_MODEL_ID'), system_prompt='test'); result = agent('hi'); print('AgentResult属性:'); print([attr for attr in dir(result) if not attr.startswith('_')]); print('\n正しいテキスト取得方法:'); print('result.message[\'content\'][0][\'text\']')"
```

**必須確認項目：**
- [ ] 利用可能な属性を確認し、公式ドキュメントと照合
- [ ] 正しいテキスト取得方法を特定（参考: `result.message['content'][0]['text']`）

### 7. 最小テストコードで動作確認

テンプレートのテストスクリプトを実行：

```bash
cd mock/
uv run python ../template/test_agent.py
```

**必須確認項目：**
- [ ] エラーなく実行できるか？
- [ ] レスポンスが正しく取得できるか？

※ `template/test_agent.py`は`mock/.env`を相対パスで読み込みます

### 8. app.pyの記法確認

**必須確認項目：**
- [ ] Agent初期化で推測パラメータを使っていないか？
- [ ] 正しいメソッドを使っているか？（`agent()` で `__call__`）
- [ ] モデルIDの形式は正しいか？
- [ ] **AgentResultから正しくテキストを取得しているか？**
  - ❌ `response.content` （このプロパティは存在しない）
  - ✅ `response.message['content'][0]['text']` （正しい方法）

## Phase 2: アプリケーション起動確認

### 9. 起動テスト（手動確認）

実装したアプリケーションを起動して、エラーなく立ち上がることを確認：

```bash
cd mock/
uv run streamlit run app.py
# または
uv run python app.py
```

**注意**: この手順は自動チェックではなく、ユーザーに起動方法を案内するのみ

**確認項目：**
- [ ] エラーなく起動するか？
- [ ] ブラウザでアクセスできるか？
- [ ] 基本的な画面が表示されるか？

### チェック完了後の報告

すべてのチェックが完了したら、以下を報告：

✅ Phase 0完了（依存関係）
✅ Phase 1完了（Strands Agents記法）
✅ Phase 2完了（起動確認）

または

❌ 修正が必要な項目
→ 正しいコードを提示

---

## 👤 参加者向けチェックリスト

### 📁 ファイル構成

- [ ] `mock/` ディレクトリが作成されている
- [ ] `mock/app.py` が存在する
- [ ] `mock/requirements.txt` が存在する
- [ ] `mock/.env` が存在する（`.env`をコピー済み）
- [ ] `mock/README.md` が存在する

### 🔧 技術要件

- [ ] Python 3.11を使用している
- [ ] `requirements.txt` に `strands-agents` が含まれている
- [ ] `requirements.txt` に `python-dotenv` が含まれている
- [ ] Streamlit または FastAPI のいずれかを使用している

### 🎯 必須機能

- [ ] ランディングページがある（サービス概要・主要機能の説明）
- [ ] メイン機能ページがある（PR/FAQで説明した主要機能の体験UI）
- [ ] Strands Agentsを使った生成AI処理が実装されている
- [ ] 処理結果を表示するページ/セクションがある

### 🚀 動作確認

- [ ] 仮想環境を作成できた（`uv venv --python 3.11`）
- [ ] 依存パッケージをインストールできた（`uv pip install -r requirements.txt`）
- [ ] アプリが起動できた（`streamlit run app.py` または `python app.py`）
- [ ] ブラウザでアクセスできた（http://localhost:8501 または http://localhost:8000）
- [ ] エラーなく画面が表示される

### 💡 機能確認

- [ ] ランディングページでサービス概要が確認できる
- [ ] メイン機能を実際に試せる
- [ ] 入力フォームやボタンが動作する
- [ ] Strands Agentsの処理が実行される（生成AI処理）
- [ ] 処理結果が表示される

### 📝 ドキュメント

- [ ] `mock/README.md` に起動手順が書かれている
- [ ] `.env` の設定方法が説明されている
- [ ] 使用している技術スタックが明記されている

### ⚠️ トラブルシューティング

#### アプリが起動しない場合

1. Python バージョンを確認
```bash
python --version  # Python 3.11.x であることを確認
```

2. `.env` ファイルが正しくコピーされているか確認
```bash
ls -la mock/.env
cat mock/.env  # API キーが設定されているか確認
```

3. 依存パッケージを再インストール
```bash
cd mock/
rm -rf .venv
uv venv --python 3.11
source .venv/bin/activate
uv pip install -r requirements.txt
```

#### Strands Agents のエラーが出る場合

1. `.env` の設定を確認
```bash
# 以下の変数が設定されているか確認
AWS_BEARER_TOKEN_BEDROCK=your-api-key-here
AWS_REGION=ap-northeast-1
AWS_BEDROCK_MODEL_ID=global.anthropic.claude-haiku-4-5-20251001-v1:0
```

2. `strands-agents` パッケージがインストールされているか確認
```bash
pip list | grep strands
```

#### 画面が表示されない場合

1. ポートが使用中でないか確認
```bash
# Streamlit の場合
lsof -i :8501

# FastAPI の場合
lsof -i :8000
```

2. ブラウザのキャッシュをクリア
3. 別のブラウザで試す

### ✅ 全てチェックできたら

おめでとうございます！モック作成が完了しました。

次のステップ：
1. **提出フォームに記入**（アイディア名、PR/FAQ、モックのURL、工夫した点）
2. **発表準備**（1分程度でアイディアとモックを紹介できるように）
3. **チームビルディング**（興味を持ってくれた人とSlackでマッチング）
