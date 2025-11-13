# 1時間アイディアソン ワークショップ

## 📋 主要ファイル

### ✅ 参加者用
- **`your_work/README.md`** - ワークガイド（参加者はここからスタート）
- **`your_work/prompts/`** - プロンプト集
- **`your_work/ideation/`** - 成果物保存先

### 📝 主催者用
- **`ideathon_v3_final.md`** - 最終設計書（90分版）
- **`README.md`** - このファイル（プロジェクト概要）

### 📁 参考資料
- **`temp/`** - 元のワークショップ資料（.gitignore）

## 🎯 プロジェクト概要

AWS ML Enablement Workshopの良いところを参照しつつ、Amazon Q Developerとの壁打ちで個人ワーク中心に90分でアイディアを膨らませ、モックを作成し、チームビルディングまで行うワークショップ。

### コンセプト
- Working Backwardsではなく、独自のアイディアソン
- Working Backwardsの良いところは継承
- 参加者のインスピレーションの種をAIで膨らませる体験

### 参加者
- 合計20人（オンライン10人 + オフライン10人）
- ほぼエンジニア、一部ビジネス職
- Amazon Q Developer初心者
- 前イベントでPython 3.11 + Strands Agent体験済み

## ⏱️ タイムテーブル（90分）

| 時間 | セクション | 内容 |
|------|-----------|------|
| 0-5分 | イントロ | 目的説明・ゴール共有・環境確認 |
| 5-35分 | アイディア膨らまし | Step1→Step2→Step3（各10分） |
| 35-60分 | モック作成 | mock-builder活用 |
| 60-65分 | 提出 | フォーム記入 |
| 65-85分 | 共有 | 発表+チームビルディング |
| 85-90分 | Next Step | Slackマッチング案内 |

## 🚀 3ステップの流れ

### Step1: 顧客理解（10分）🤖
- ペルソナ作成
- 行動分析
- 課題の特定

### Step2: アイディア発明（10分）🤖
- 参考事例収集
- アイディア発明（3つ）
- 最有望案の選択

### Step3: ビジネス化（10分）🤖
- ビジネスモデルキャンバス（オプション）
- 簡易PR/FAQ（必須）
- 検証ポイント

## 📂 ファイル構成

```
ai-hackathon-2025-ideathon/
├── README.md                              # このファイル
├── ideathon_v3_final.md                  # 最終設計書
├── LICENSE                               # MIT-0ライセンス
├── your_work/                            # 参加者用ワークスペース
│   ├── README.md                         # ワークガイド
│   ├── .amazonq/cli-agents/              # Agent設定
│   │   ├── default-agent.json            # 壁打ち相手用
│   │   └── mock-builder.json             # モック作成用
│   ├── prompts/                          # プロンプト集
│   │   ├── step1_customer_understanding.md
│   │   ├── step2_idea_invention.md
│   │   ├── step3_business_model.md
│   │   └── mock_creation.md
│   ├── ideation/                         # 成果物保存先
│   │   ├── step1_persona.md
│   │   ├── step2_ideas.md
│   │   └── step3_prfaq.md                # モック作成時に参照
│   └── template/                         # Reactテンプレート
└── temp/                                 # 参考資料（.gitignore）
```

## 🎯 参加者の始め方

1. リポジトリをクローン
2. **`your_work/README.md`** を開く
3. ガイドに沿って進める

## 📝 メモ

- ビジネスモデルキャンバスはオプション（時間がある人だけ）
- モックは「ポン出し」レベルでOK
- PR/FAQは必須
- チームビルディングが本番

## 🙏 Acknowledgments

このプロジェクトは [AWS ML Enablement Workshop](https://github.com/aws-samples/aws-ml-enablement-workshop) を参考にしています。
