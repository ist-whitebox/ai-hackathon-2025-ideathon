# 90分アイディアソン ワークガイド

このガイドでは、Amazon Q Developerとの壁打ちで90分でアイディアを膨らませ、モックを作成するまでの流れを説明します。

## 🎯 ゴール

- 身近な課題からアイディアを発明する
- PR/FAQを作成する
- 動くモック（ポン出しレベル）を作成する
- チームビルディングのきっかけを作る

## ⏱️ タイムテーブル

| 時間 | 内容 |
|------|------|
| 0-5分 | イントロ・環境確認 |
| 5-35分 | アイディア膨らまし（Step1→2→3） |
| 35-60分 | モック作成 |
| 60-65分 | 提出 |
| 65-85分 | 共有・チームビルディング |
| 85-90分 | Next Step |

## 📂 ディレクトリ構成

```
your_work/
├── README.md              # このファイル
├── prompts/               # プロンプト集
│   ├── step1_customer_understanding.md
│   ├── step2_idea_invention.md
│   ├── step3_business_model.md
│   └── mock_creation.md
├── ideation/              # 成果物保存先
│   ├── step1_persona.md
│   ├── step2_ideas.md
│   └── step3_prfaq.md    # モック作成時に参照
└── template/              # Reactテンプレート（mock-builderが使用）
```

## 🚀 作業の流れ

### 事前準備

1. リポジトリをクローン
```bash
git clone <repository-url>
cd ai-hackathon-2025-ideathon/your_work
```

2. 現在のディレクトリを確認
```bash
pwd
# /path/to/ai-hackathon-2025-ideathon/your_work を期待
```

3. Amazon Q Developer CLIを起動
```bash
q chat
# または q
```

### Step1: 顧客理解（10分）🤖

**目的**: 身近な課題から顧客像を作り、行動を分析し、改善すべき課題を特定する

1. `prompts/step1_customer_understanding.md` を開く
2. プロンプトをコピーし、`[ここに課題を記入]` を自分の課題に置き換え
3. Amazon Q Developer (`q chat`) に貼り付け
4. 出力結果を確認し、必要に応じて追加質問
5. **結果を `ideation/step1_persona.md` に保存**

**期待されるアウトプット:**
- ペルソナ（顧客像）
- 行動の時系列マップ
- 改善すべき課題Top3

### Step2: アイディア発明（10分）🤖

**目的**: 参考事例を収集し、組み合わせて新しい解決策を発明する

1. `prompts/step2_idea_invention.md` を開く
2. プロンプトをコピー
3. Amazon Q Developer (`q chat`) に貼り付け
4. 出力結果を確認し、必要に応じて追加質問
5. **結果を `ideation/step2_ideas.md` に保存**

**期待されるアウトプット:**
- 参考事例5つ
- 発明したアイディア3つ
- 選択した最有望案1つ

**参考リンク:**
- [AWS生成AI事例集](https://aws.amazon.com/jp/local/genai-4-jp/)

### Step3: ビジネス化（10分）🤖

**目的**: 選択したアイディアをビジネスとして成立させるための分析を行う

1. `prompts/step3_business_model.md` を開く
2. プロンプトをコピー
3. Amazon Q Developer (`q chat`) に貼り付け
4. 出力結果を確認し、必要に応じて追加質問
5. **結果を `ideation/step3_prfaq.md` に保存（重要！）**

**期待されるアウトプット:**
- ビジネスモデルキャンバス（オプション）
- 簡易PR/FAQ（必須）

**重要:**
- ビジネスモデルキャンバスはオプション（時間がない場合はスキップ）
- **PR/FAQは必須**（モック作成の元になります）

### モック作成（25分）🤖

**目的**: PR/FAQから動くモック（ポン出しレベル）を作成する

1. `your_work` ディレクトリにいることを確認
```bash
pwd
# /path/to/ai-hackathon-2025-ideathon/your_work を期待
```

2. mock-builderエージェントを起動
```bash
q chat --agent mock-builder
```

3. 「モックを作成したい」と入力

4. 技術スタックを選択（Streamlit または FastAPI+HTML）

5. 自動的に `mock/` ディレクトリにアプリが生成されます

6. 仮想環境を作成して起動
```bash
cd mock/
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt

# Streamlitの場合
streamlit run app.py

# FastAPIの場合
python app.py
```

7. ブラウザで開く
- Streamlit: http://localhost:8501
- FastAPI: http://localhost:8000

**期待されるアウトプット:**
- ランディングページ
- 動作するアプリケーション（モックレベル）
- ローカルURL

### 提出（5分）📝

1. 提出フォームに以下を記入
   - アイディア名
   - PR/FAQ
   - モックのURL
   - 工夫した点

### 共有・チームビルディング（20分）🎉

1. 発表者選定（各自1分）
2. 発表
3. 興味のあるアイディアにリアクション
4. Slackでマッチング

## 💡 Tips

### プロンプトの使い方
- プロンプトはテンプレートです。自分の状況に合わせて編集してください
- Amazon Q Developerとの対話は壁打ちです。遠慮なく質問してください
- 出力結果が気に入らなければ、「もっと具体的に」「別の案を」と追加質問

### 時間配分
- Step1-3で各10分を目安に
- 時間がなければビジネスモデルキャンバスはスキップ
- PR/FAQは必ず作成（モック作成に必要）

### モック作成
- 「ポン出し」レベルでOK
- 完璧を目指さない
- デザインよりも機能の体験を優先

### トラブルシューティング

#### Amazon Q Developer CLIが起動しない
```bash
# インストール確認
q --version

# 再インストール
npm install -g @aws/amazon-q-developer-cli
```

#### モック作成が失敗する
- `ideation/step3_prfaq.md` が保存されているか確認
- PR/FAQの内容が具体的か確認
- エラーメッセージをAmazon Q Developerに貼り付けて相談

#### AWSデプロイが失敗する
- AWS CLIの設定を確認
```bash
aws sts get-caller-identity
```

## 📚 参考資料

- [Amazon Q Developer ドキュメント](https://docs.aws.amazon.com/amazonq/)
- [AWS生成AI事例集](https://aws.amazon.com/jp/local/genai-4-jp/)

## 🙏 Acknowledgments

このワークショップは [AWS ML Enablement Workshop](https://github.com/aws-samples/aws-ml-enablement-workshop) を参考にしています。
