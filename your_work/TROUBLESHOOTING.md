# ⚠️ トラブルシューティング

ワークショップ中に問題が発生した場合は、まず**運営・チューターに相談**してください。

このドキュメントは、よくある問題の解決方法をまとめたリファレンスです。

---

## 🔧 環境関連

### Amazon Q Developer拡張機能が動かない

1. **拡張機能のインストール確認**
   - VSCode左側の拡張機能アイコンをクリック
   - 「Amazon Q」で検索
   - インストールされているか確認

2. **再起動**
   - VSCodeを再起動

3. **ログイン確認**
   - Amazon Qアイコンをクリック
   - ログイン状態を確認

### Python環境の問題

**Python バージョンを確認**

```bash
python --version  # Python 3.11.x であることを確認
```

**uvが動かない**

```bash
# uvを再インストール
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 📝 モック作成関連

### モック作成が失敗する

- `ideation/step3_prfaq.md` が保存されているか確認
- PR/FAQの内容が具体的か確認
- エラーメッセージをAmazon Q Developerチャットに貼り付けて相談

### アプリが起動しない

1. **.envファイルが正しくコピーされているか確認**

```bash
ls -la mock/.env
cat mock/.env  # API キーが設定されているか確認
```

2. **依存パッケージを再インストール**

```bash
cd mock/
rm -rf .venv
uv venv --python 3.11
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

### Strands Agentsのエラーが出る

1. **.envの設定を確認**

```bash
# 以下の変数が設定されているか確認
AWS_BEARER_TOKEN_BEDROCK=your-api-key-here
AWS_REGION=ap-northeast-1
AWS_BEDROCK_MODEL_ID=global.anthropic.claude-haiku-4-5-20251001-v1:0
```

2. **strands-agentsパッケージがインストールされているか確認**

```bash
pip list | grep strands
```

---

## 🖥️ 起動・表示関連

### 画面が表示されない

1. **ポートが使用中でないか確認**

```bash
# Streamlit の場合
lsof -i :8501

# FastAPI の場合
lsof -i :8000
```

使用中の場合は、プロセスを終了：

```bash
# プロセスIDを確認
lsof -i :8501

# プロセスを終了（PIDは上記で確認した番号）
kill -9 [PID]
```

2. **ブラウザのキャッシュをクリア**

3. **別のブラウザで試す**

---

## 🎨 プレゼン生成関連

### エラー: 成果物ファイルが不足しています

**原因**: Step1-3の成果物が保存されていない

**解決方法**:
```bash
# ファイルの存在を確認
ls -la ideation/

# 必要なファイル:
# - step1_persona.md
# - step2_ideas.md
# - step3_prfaq.md
```

### AIの処理がうまくいかない

- `.env` ファイルが `your_work/` にあるか確認
- APIキーが正しく設定されているか確認
- 運営に相談

---

## 🆘 それでも解決しない場合

### 即座にサポートを受ける方法

1. **オフライン参加者**: 手を挙げて運営・チューターを呼ぶ
2. **オンライン参加者**: Slackで質問する
3. **エラーメッセージをコピー**: 正確なエラー内容を共有する

### 参考資料

- [Amazon Q Developer ドキュメント](https://docs.aws.amazon.com/amazonq/)
- [前回ハンズオン資料](https://github.com/ist-whitebox/ai-hackathon-2025-hands-on)
- [Streamlit公式ドキュメント](https://docs.streamlit.io/)

---

## 💡 予防策

### 事前確認チェックリスト

ワークショップ開始前に以下を確認しておくと、トラブルを防げます：

- [ ] Python 3.11がインストールされている
- [ ] uvがインストールされている
- [ ] Amazon Q Developer拡張機能がVSCodeにインストールされている
- [ ] Amazon Q Developerにログインできる
- [ ] `.env`ファイルが設定されている
- [ ] 前回のハンズオン環境が動作する

---

**💬 困ったら、遠慮なく運営・チューターに相談してください！**


