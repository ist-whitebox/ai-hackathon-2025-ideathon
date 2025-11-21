# 🎯 90分アイディアソン ワークショップ手順書

このワークショップでは、Amazon Q Developerとの壁打ちで90分でアイディアを膨らませ、モックを作成し、チームビルディングまで行います。

## 📋 全体の流れ（90分）

```
0-5分   ► イントロ・環境確認
5-35分  ► アイディア膨らまし（Step1→2→3）
35-60分 ► モック作成（Step4）
60-65分 ► スライド作成（Step6）
65-70分 ► 提出（Step7）
70-85分 ► 共有・チームビルディング
85-90分 ► Next Step
```

---

## 🔧 事前準備（開始前に完了させる）

### 1. 環境確認

```bash
python --version  # Python 3.11.x を期待
uv --version
```

- Amazon Q Developer拡張機能がVSCodeにインストールされていることを確認
- VSCodeでAmazon Qチャットが開けることを確認

### 2. リポジトリのクローン

```bash
git clone https://github.com/ist-whitebox/ai-hackathon-2025-ideathon.git
cd ai-hackathon-2025-ideathon
```

### 3. .envファイルの設定

```bash
cp your_work/.env.sample your_work/.env
```

`your_work/.env`ファイルを編集し、運営から配布されたAPIキーを設定してください。

### 4. 身近な課題を考える

アイディアの種となる「身近な課題」を1つ考えておいてください（メモ程度でOK）。

---

## 📍 重要: 作業ディレクトリについて

このワークショップでは、**最初から最後まで同じフォルダで作業**します。

### VSCodeで開くフォルダ
**`ai-hackathon-2025-ideathon/`** （ルートディレクトリ）

### Amazon Q設定の切り替え

- **Step1-3（アイディア膨らまし）**: 自動的にルートの設定が適用されます
- **Step4（モック作成）**: プロンプトで設定ファイルを明示的に指定します

💡 **ポイント**: フォルダ切り替えは不要です。プロンプトで設定を指定することで、適切なAIサポートが得られます

---

## 💡 基本的な流れ（Step1-3共通）

### Amazon Q Developerチャットの開き方

- VSCode左側のAmazon Qアイコンをクリック
- またはショートカット: `Cmd+Shift+P` (Mac) / `Ctrl+Shift+P` (Win) → 「Amazon Q: Open Chat」

### プロンプトの使い方

1. `your_work/prompts/stepN_xxx.md` を開く
2. プロンプトをコピー
3. Amazon Qチャットに貼り付けて実行
4. 出力結果を確認
5. 必要に応じて追加質問
6. 結果を `your_work/ideation/stepN_xxx.md` に保存

### レビューのポイント

**AIの出力をそのまま受け入れず、自分の頭で考えることが重要です。**

- 内容が自分の意図と合っているか確認
- 不足している情報はないか確認
- 必要に応じてファイルを直接編集

---

## Step 1: 顧客理解 🤖

**目的**: 身近な課題から顧客像を作り、行動を分析し、改善すべき課題を特定する

### 作業手順

1. **VSCodeで正しいフォルダを開く**
   ```
   File > Open Folder → ai-hackathon-2025-ideathon/ を選択
   ```

2. **プロンプトを実行**
   - `your_work/prompts/step1_customer_understanding.md` を開く
   - `[ここに自分の課題を記入]` を実際の課題に置き換える
   - プロンプトをコピーしてAmazon Qチャットに貼り付け
   - Claude Sonnet 4.5を利用するようにしましょう

3. **出力結果を保存**
   - `your_work/ideation/step1_persona.md` に保存

4. **レビュー・修正**
   - [ ] ペルソナは自分が想定する顧客像と合っているか？
   - [ ] 行動分析は現実的か？
   - [ ] 課題Top3は本当に重要か？

### 期待されるアウトプット

- ✅ ペルソナ（顧客像）
- ✅ 行動の時系列マップ
- ✅ 改善すべき課題Top3

---

## Step 2: アイディア発明 🤖

**目的**: 参考事例を収集し、組み合わせて新しい解決策を発明する

### 作業手順

1. **プロンプトを実行**
   - `your_work/prompts/step2_idea_invention.md` を開く
   - プロンプトにはStep1の結果が自動参照される（`@your_work/ideation/step1_persona.md`）

2. **出力結果を保存**
   - `your_work/ideation/step2_ideas.md` に保存

3. **レビュー・修正**
   - [ ] 参考事例は本当に参考になるか？
   - [ ] 3つのアイディアは課題を解決できているか？
   - [ ] 最有望案の選択理由は納得できるか？

### 期待されるアウトプット

- ✅ 参考事例5つ
- ✅ 発明したアイディア3つ
- ✅ 選択した最有望案1つ

**参考**: [AWS生成AI事例集](https://aws.amazon.com/jp/local/genai-4-jp/)

---

## Step 3: ビジネス化 🤖

**目的**: 選択したアイディアをビジネスとして成立させるための分析を行う

### 作業手順

1. **プロンプトを実行**
   - `your_work/prompts/step3_business_model.md` を開く
   - プロンプトにはStep2の結果が自動参照される（`@your_work/ideation/step2_ideas.md`）

2. **出力結果を保存（重要！）**
   - `your_work/ideation/step3_prfaq.md` に保存
   - **このファイルはモック作成時に参照されます**

3. **レビュー・修正**
   - [ ] サービス名は魅力的か？
   - [ ] 解決する課題は明確か？
   - [ ] 体験手順はシンプルか？
   - [ ] 独自の強みは明確か？

### 重要

- **ビジネスモデルキャンバスはオプション**: 時間がない場合はスキップしてOK
- **PR/FAQは必須**: これがモック作成の元になります

### 期待されるアウトプット

- ✅ ビジネスモデルキャンバス（オプション）
- ✅ PR/FAQ（必須）

---

## Step 4: モック作成 🤖

**目的**: PR/FAQからStrands Agentsを活用した動くモックを作成する

### 作業手順

1. **Amazon Q Developerチャットを開く**

2. **モック作成を依頼（重要：設定ファイルを指定）**
   
   以下をコピーして、Amazon Qチャットに貼り付けてください：
   
   ```
   your_work/.amazonq/default.json を確認して作業してください。モックを作りたいです。
   ```
   
   ⚠️ **重要**: この指定により、モック作成専用のAI設定が適用されます

3. **技術スタックを選択**
   - **推奨**: Streamlit + Strands Agents（最速で実装可能）
   - オプション: FastAPI + HTML + Strands Agents

3. **.envファイルをコピー**
   ```bash
   cp your_work/.env your_work/mock/.env
   ```

4. **仮想環境を作成して起動**
   ```bash
   cd your_work/mock/
   uv venv --python 3.11
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   uv pip install -r requirements.txt
   
   streamlit run app.py  # Streamlitの場合
   # または
   python app.py         # FastAPIの場合
   ```

5. **ブラウザで確認**
   - Streamlit: http://localhost:8501
   - FastAPI: http://localhost:8000

### モック完成後の確認（必須）

Amazon Q Developerチャットで以下を実行：

```
your_work/.amazonq/mock-builder/CHECKLIST.md に沿ってチェックしてください
```

期待される結果：
- ✅ Phase 0完了（依存関係）
- ✅ Phase 1完了（Strands Agents記法）
- ✅ Phase 2完了（起動確認）

### 期待されるアウトプット

- ✅ ランディングページ
- ✅ メイン機能ページ
- ✅ Strands Agentsを活用した生成AI処理
- ✅ 動作するアプリケーション

**💡 シンプルでOK - 完璧を求めず、動けばOKです**

---

## Step 5: モック微調整（オプション）

時間があれば、Amazon Qチャットで以下のような依頼をしてモックを改善できます：

- 「ランディングページのレイアウトを3カラムに変更してください」
- 「結果をCSVでダウンロードできる機能を追加してください」
- 「入力が空の場合のエラーメッセージを追加してください」

**一度に1つずつ変更を依頼し、変更後は必ず動作確認してください。**

---

## Step 6: スライド作成（5分）

**目的**: Step1-3とモックの成果物から、プレゼン資料を自動生成する

### 作業手順

モックで使った仮想環境を使用します。

**ルートディレクトリ (`ai-hackathon-2025-ideathon/`) から実行：**

```bash
cd your_work/mock/
source .venv/bin/activate  # Windows: .venv\Scripts\activate

cd ../presentation/
python generate.py
```

デザインを選択（4つの質問に答える）

生成完了後、`your_work/presentation/index.html` をブラウザで開いて確認

**💡 発表はブラウザのフルスクリーンモード（F11）で行うとプロフェッショナルです**

---

## Step 7: 提出 📝

Slackチャンネルに、以下を投稿してください：

**1. テキストメッセージ:**

```
【氏名】
[ここに名前を記入]

【サービス名】
[ここにサービス名を記入]

【説明】
[50文字〜100文字程度でサービス概要と想いを記入]

【チームメンバー募集】
[Yes / No]
```

**2. 添付ファイル（必須）:**

テキストメッセージと一緒に、以下のファイルをドラッグ&ドロップで添付してください：

- 📄 **成果物ファイル**: `your_work/ideation/` 以下のmdファイル（Step1-3）
- 🖼️ **モックのスクショ**: 動作している画面のキャプチャ
- 📊 **スライドのスクショ**: `your_work/presentation/index.html` のキャプチャ

**提出期限: 70分まで**

---

## Step 8: 発表準備

全員が順番に発表します。発表の準備をしてください。

### 発表フォーマット（2分）

1. **課題と顧客**（20秒） - 誰のどんな課題を解決するか
2. **解決策の概要**（40秒） - サービスの主要機能と独自の強み
3. **モックデモ**（50秒） - 画面共有でモックを実際に操作
4. **募集の呼びかけ**（10秒） - チームメンバーを募集する場合

**💡 スライドを使って視覚的に説明し、モックは実際に動かして見せてください**

---

## Step 9: 共有・チームビルディング 🎉

### 発表

全員が順番に2分ずつ発表します。

### チームビルディング

1. 運営が全員の「想い」一覧を画面共有
2. 気になるアイディアに声をかける
3. Slackでマッチング継続

---

## Step 10: Next Step

### 今後の展開

1. **Slackでの継続マッチング** - 全アイディア一覧を後日公開
2. **次回ハッカソンでの実装** - チームで実際に開発
3. **チームでの開発継続** - 実際のサービスリリースを目指す

---

## ⚠️ トラブルシューティング

問題が発生した場合は、**運営・チューターに相談**してください。

よくある問題の詳細な解決方法は **[TROUBLESHOOTING.md](./TROUBLESHOOTING.md)** を参照してください。

---

## 📚 参考資料

- [Amazon Q Developer ドキュメント](https://docs.aws.amazon.com/amazonq/)
- [AWS生成AI事例集](https://aws.amazon.com/jp/local/genai-4-jp/)
- [Streamlit公式ドキュメント](https://docs.streamlit.io/)
- [前回ハンズオン資料](https://github.com/ist-whitebox/ai-hackathon-2025-hands-on)
- [トラブルシューティング](./TROUBLESHOOTING.md)

---

## ✅ 全てチェックできたら

おめでとうございます！アイディアソンが完了しました。

**持ち帰れるもの:**
- ✅ PR/FAQ（仕様書）
- ✅ ビジネスモデルキャンバス（オプション）
- ✅ モック
- ✅ 発表用スライド
- ✅ チームメンバー候補
- ✅ 次のステップへの道筋

**次のステップ:**
- Slackでチームメンバーとマッチング
- 次回ハッカソンで実装
- 実際のサービスリリースを目指す

---

## 🙏 Acknowledgments

このワークショップは [AWS ML Enablement Workshop](https://github.com/aws-samples/aws-ml-enablement-workshop) を参考にしています。
