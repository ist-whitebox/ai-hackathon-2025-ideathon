# チェックリスト ✅

モックアプリケーションが完成したら、以下のチェックリストで確認してください。

---

## 🤖 Amazon Q Developer向け検証手順

**ユーザーから「チェックリストに沿ってチェックをしてください」と依頼されたら、以下を実行してください。**

## Phase 0: 依存関係の確認

### 1. requirements.txtの確認

**必須確認項目：**
- [ ] `strands-agents`が含まれているか？
- [ ] 選択した技術スタック（`streamlit`または`fastapi`+`uvicorn`）が含まれているか？
- [ ] `python-dotenv`が含まれているか？

### 2. 仮想環境とインストール

```bash
cd mock/
uv venv --python 3.11
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

**確認項目：**
- [ ] エラーなくインストールできるか？

## Phase 1: Strands Agents記法の検証（最優先）

### 3. Strands APIの確認

```bash
cd mock/
source .venv/bin/activate
python -c "import strands; print(dir(strands))"
```

### 4. Agent初期化パラメータの確認

```bash
python -c "from strands import Agent; help(Agent.__init__)"
```

**必須確認項目：**
- [ ] 使用可能なパラメータ名を確認
- [ ] `name`パラメータは存在するか？
- [ ] `instructions`パラメータは存在するか？
- [ ] `system_prompt`パラメータは存在するか？

### 5. Agent利用可能メソッドの確認

```bash
python -c "from strands import Agent; print([m for m in dir(Agent) if not m.startswith('_')])"
```

**必須確認項目：**
- [ ] `run()`メソッドは存在するか？
- [ ] `stream_async()`メソッドは存在するか？

### 6. 最小テストコードで動作確認

テンプレートのテストスクリプトを実行：

```bash
cd ../template/
python test_agent.py
```

**必須確認項目：**
- [ ] エラーなく実行できるか？
- [ ] レスポンスが正しく取得できるか？

※ `template/test_agent.py`は`mock/.env`を相対パスで読み込みます

### 7. app.pyの記法確認

**必須確認項目：**
- [ ] Agent初期化で推測パラメータを使っていないか？
- [ ] 正しいメソッドを使っているか？
- [ ] モデルIDの形式は正しいか？

## Phase 2: アプリケーション起動確認

### 8. 起動テスト

実装したアプリケーションを起動して、エラーなく立ち上がることを確認：

```bash
# 実装に応じたコマンドで起動
python app.py
# または
streamlit run app.py
```

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
