# 1時間アイディアソン ワークショップ

## 📋 主要ファイル

### ✅ 参加者用
- **`your_work/WORKSHOP.md`** - 詳細手順書（参加者はここからスタート）
- **`your_work/README.md`** - 簡易ガイド（概要とファイル構成）
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
- 前イベントでPython 3.11 + Strands Agents体験済み

## 🚀 3ステップの流れ

### Step1: 顧客理解 🤖
- ペルソナ作成
- 行動分析
- 課題の特定

### Step2: アイディア発明 🤖
- 参考事例収集
- アイディア発明（3つ）
- 最有望案の選択

### Step3: ビジネス化 🤖
- ビジネスモデルキャンバス（オプション）
- PR/FAQ（必須）
- 検証ポイント

## 🤖 Amazon Q設定の工夫

このワークショップでは、**2つの異なるAmazon Q設定**を使い分けることで、最適なAIサポートを実現しています：

### ルートディレクトリ (`.amazonq/default.json`)
- **用途**: Step1-3（アイディア膨らまし）
- **振る舞い**: 壁打ち相手として、顧客理解・アイディア発明・ビジネス化をサポート
- **VSCodeで開くフォルダ**: `ai-hackathon-2025-ideathon/`

### your_workディレクトリ (`your_work/.amazonq/`)
- **用途**: Step4（モック作成）
- **振る舞い**: mock-builderとして、PR/FAQからモックを自動生成
- **VSCodeで開くフォルダ**: `ai-hackathon-2025-ideathon/your_work/`

💡 **ポイント**: 作業内容に応じてVSCodeで開くフォルダを変えることで、最適なAIサポートが得られます

## ⏱️ タイムテーブル

詳細なタイムテーブルは **[WORKSHOP.md](./your_work/WORKSHOP.md)** を参照してください。

## 📂 ファイル構成

```
ai-hackathon-2025-ideathon/
├── README.md                              # このファイル
├── ideathon_v3_final.md                  # 最終設計書
├── LICENSE                               # MIT-0ライセンス
├── .amazonq/
│   └── default.json                      # アイディア膨らまし用（Step1-3）
├── your_work/                            # 参加者用ワークスペース
│   ├── README.md                         # ワークガイド
│   ├── .amazonq/
│   │   ├── default.json                  # モック作成用（Step4）
│   │   └── mock-builder/                 # エージェント専用リソース
│   │       ├── IMPROVEMENT_GUIDE.md
│   │       └── mock_builder_prompt.md
│   ├── prompts/                          # プロンプト集
│   │   ├── step1_customer_understanding.md
│   │   ├── step2_idea_invention.md
│   │   └── step3_business_model.md
│   ├── ideation/                         # 成果物保存先
│   │   ├── step1_persona.md
│   │   ├── step2_ideas.md
│   │   └── step3_prfaq.md                # モック作成時に参照
│   ├── presentation/                     # プレゼン資料生成（Step6）
│   │   ├── generate.py                   # 自動生成スクリプト
│   │   ├── README.md                     # 使い方ガイド
│   │   └── index.html                    # 生成されたプレゼン
│   └── template/                         # テンプレート
└── temp/                                 # 参考資料（.gitignore）
```

## 🎯 参加者の始め方

1. リポジトリをクローン
2. **`your_work/WORKSHOP.md`** を開く（詳細手順書）
3. ガイドに沿って進める

**クイックリンク:**
- 📖 [詳細手順書](./your_work/WORKSHOP.md) - ステップバイステップガイド
- 📋 [簡易ガイド](./your_work/README.md) - 概要とファイル構成

## 📝 メモ

- ビジネスモデルキャンバスはオプション（時間がある人だけ）
- モックはシンプルでOK
- PR/FAQは必須
- チームビルディングが本番

## 🙏 Acknowledgments

このプロジェクトは [AWS ML Enablement Workshop](https://github.com/aws-samples/aws-ml-enablement-workshop) を参考にしています。
