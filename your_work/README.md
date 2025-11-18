# 参加者用ワークスペース

## 🚀 クイックスタート

**👉 [WORKSHOP.md](./WORKSHOP.md) を開いて手順に従ってください**

このワークスペースには、90分アイディアソンに必要なすべてのリソースが含まれています。

## 🎯 ゴール

- 身近な課題からアイディアを発明する
- PR/FAQを作成する
- 動くモックを作成する
- チームビルディングのきっかけを作る

## 📂 ファイル構成

```
your_work/
├── README.md              # このファイル（簡易ガイド）
├── WORKSHOP.md            # 📖 詳細手順書（メインガイド）

├── .amazonq/
│   ├── default.json       # モック作成用エージェント設定
│   └── mock-builder/      # エージェント専用リソース
├── prompts/               # プロンプト集
│   ├── step1_customer_understanding.md
│   ├── step2_idea_invention.md
│   └── step3_business_model.md
├── ideation/              # 成果物保存先
│   ├── step1_persona.md
│   ├── step2_ideas.md
│   └── step3_prfaq.md    # モック作成時に参照
├── presentation/          # プレゼン資料生成
│   ├── generate.py        # プレゼン自動生成スクリプト
│   ├── README.md          # 使い方ガイド
│   └── index.html         # 生成されたプレゼン（実行後）
└── template/              # テンプレート・サンプルコード
```

## 📋 主要ドキュメント

- **[WORKSHOP.md](./WORKSHOP.md)** - 詳細手順書（ステップバイステップガイド）
- **`prompts/`** - 各ステップのプロンプトテンプレート
- **`template/`** - Streamlit/FastAPIのサンプルコード

## ⏱️ タイムテーブル

詳細なタイムテーブルは **[WORKSHOP.md](./WORKSHOP.md)** を参照してください。

## 🔧 事前準備

開始前に以下を確認してください：

- [ ] Python 3.11がインストールされている
- [ ] Amazon Q Developer CLIが動作する
- [ ] リポジトリをクローンした
- [ ] `.env`ファイルを設定した（APIキー）
- [ ] 身近な課題を1つ考えた

詳細は **[WORKSHOP.md](./WORKSHOP.md)** の「事前準備」セクションを参照してください。

## 🎯 ワークショップの流れ

詳細な手順は **[WORKSHOP.md](./WORKSHOP.md)** を参照してください。

### Step 1-3: アイディア膨らまし

1. **Step1: 顧客理解** - ペルソナ作成、行動分析、課題特定
2. **Step2: アイディア発明** - 参考事例収集、アイディア発明
3. **Step3: ビジネス化** - PR/FAQ作成（必須）

### Step 4: モック作成

- Streamlit または FastAPI でモック作成
- Strands Agentsで生成AI処理を実装
- チェックリストで検証

### Step 6-8: プレゼン・提出・発表

- **Step6**: プレゼン資料を自動生成（5分）
- **Step7**: 提出フォーム記入
- **Step8**: 発表・チームビルディング

## ⚠️ 重要: 作業ディレクトリ

Amazon Q Developerは作業ディレクトリを基準に動作します。

- **Step1-3（アイディア膨らまし）**: `ai-hackathon-2025-ideathon/`
- **Step4（モック作成）**: `ai-hackathon-2025-ideathon/your_work/`

詳細は **[WORKSHOP.md](./WORKSHOP.md)** の「作業ディレクトリについて」セクションを参照してください。

## 💡 重要なポイント

- **VSCode拡張機能を使う** - 初心者に推奨（CLI版はオプション）
- **シンプルでOK** - 完璧を求めない
- **PR/FAQは必須** - モック作成の元になる
- **時間配分を守る** - タイムテーブルに沿って進める
- **AIと壁打ち** - 遠慮なく質問・追加依頼する

## ⚠️ トラブルシューティング

問題が発生した場合は **[WORKSHOP.md](./WORKSHOP.md)** の「トラブルシューティング」セクションを参照してください。

または運営・チューターに質問してください。

## 📚 参考資料

- **[WORKSHOP.md](./WORKSHOP.md)** - 詳細手順書（タイムテーブル含む）
- [Amazon Q Developer ドキュメント](https://docs.aws.amazon.com/amazonq/)
- [AWS生成AI事例集](https://aws.amazon.com/jp/local/genai-4-jp/)
- [Streamlit公式ドキュメント](https://docs.streamlit.io/)

---

**👉 まずは [WORKSHOP.md](./WORKSHOP.md) を開いて始めましょう！**
