# モック作成の失敗を防ぐための改善ガイド

## 今回発生した問題

1. `strands_agents` → `strands` のインポート名の誤り
2. `Agent`の初期化パラメータ（`instructions` → `system_prompt`）の誤り
3. `Task`クラスが存在しない
4. `agent.run()` → `agent.invoke_async()` のメソッド名の誤り
5. `result.content` → `result.message['content'][0]['text']` の戻り値構造の誤り

## 根本原因

**ライブラリのAPI仕様を確認せずに、推測で実装を進めた**

## 改善策

### 1. プロンプトの改善

`prompts/mock_builder_prompt.md` に以下のセクションを追加：

```markdown
## 実装前の必須確認事項

### ステップ1: ライブラリAPI調査（必須）

実装を開始する前に、以下のコマンドで使用するライブラリのAPI仕様を確認してください：

```bash
# 1. インポート可能なモジュール/クラスの確認
python -c "import strands; print(dir(strands))"

# 2. クラスの初期化パラメータの確認
python -c "from strands import Agent; help(Agent.__init__)"

# 3. 利用可能なメソッドの確認
python -c "from strands import Agent; a = Agent(); print([m for m in dir(a) if not m.startswith('_')])"

# 4. 戻り値の構造確認（実際に実行）
python -c "
from strands import Agent
import asyncio
a = Agent()
result = asyncio.run(a.invoke_async('test'))
print('Result type:', type(result))
print('Message type:', type(result.message))
print('Message structure:', result.message)
"
```

### ステップ2: 小さなテストコードで検証

本実装の前に、最小限のテストコードで動作確認：

```python
# test_strands.py
from strands import Agent
import asyncio

async def test():
    agent = Agent(system_prompt="You are a helpful assistant.")
    result = await agent.invoke_async("Hello")
    print(result.message['content'][0]['text'])

asyncio.run(test())
```

### ステップ3: 確認した仕様に基づいて実装

調査結果を元に、正確なコードを記述する。
```

### 2. エージェント設定の改善

`.amazonq/cli-agents/mock-builder.json` の `prompt` セクションを以下のように修正：

```json
{
  "prompt": "あなたは経験豊富なPython開発者です。

【重要】実装前に必ず以下を実行してください：
1. 使用するライブラリ（strands-agents）のAPI仕様を確認
   - execute_bashツールで `python -c \"import strands; print(dir(strands))\"` を実行
   - Agentクラスの初期化パラメータを `help(Agent.__init__)` で確認
   - 利用可能なメソッドを確認
   - 戻り値の構造を実際に実行して確認
2. 小さなテストコードで動作確認
3. 確認した仕様に基づいて本実装

file://.amazonq/mock-builder/mock_builder_prompt.md の指示に従って、file://ideation/step3_prfaq.md のPR/FAQを基にモックアプリケーションを作成してください。"
}
```

### 3. mock_builder_prompt.mdの改善

以下の内容を追加：

```markdown
## 実装フロー

### Phase 0: API仕様確認（新規追加）

1. strands-agentsのインポート確認
2. Agentクラスの初期化パラメータ確認
3. 利用可能なメソッド確認
4. 戻り値の構造確認
5. 小さなテストコードで動作確認

### Phase 1: ディレクトリ構成作成
...（既存の内容）

### Phase 2: 実装
確認したAPI仕様に基づいて実装
...
```

## 具体的な修正例

### Before（推測ベース）
```python
from strands_agents import Agent, Task  # ❌ 推測

agent = Agent(
    instructions="...",  # ❌ 推測
    model="..."  # ❌ 推測
)

task = Task(description="...", agent=agent)  # ❌ 推測
result = task.execute()  # ❌ 推測
text = result.output  # ❌ 推測
```

### After（確認ベース）
```python
# 事前確認: python -c "import strands; print(dir(strands))"
from strands import Agent  # ✅ 確認済み

# 事前確認: help(Agent.__init__)
agent = Agent(
    system_prompt="..."  # ✅ 確認済み
)

# 事前確認: dir(agent) で invoke_async を確認
result = await agent.invoke_async("...")  # ✅ 確認済み

# 事前確認: 実際に実行して result.message の構造を確認
text = result.message['content'][0]['text']  # ✅ 確認済み
```

## まとめ

### 失敗の原因
- **推測で実装** → エラーの連続

### 成功のための原則
- **確認してから実装** → 一発で動く

### 実装前のチェックリスト
- [ ] ライブラリのインポート名を確認した
- [ ] クラスの初期化パラメータを確認した
- [ ] 利用可能なメソッドを確認した
- [ ] 戻り値の構造を確認した
- [ ] 小さなテストコードで動作確認した
- [ ] 本実装を開始する

**「確認に5分、実装に5分」の方が「推測で実装して30分デバッグ」より速い**
