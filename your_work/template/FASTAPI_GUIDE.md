# FastAPI + HTML モックアプリケーション ガイド

## 概要

このガイドでは、FastAPI + HTMLを使用したモックアプリケーションの作成方法を説明します。

## 技術スタック

- Python 3.11+
- FastAPI 0.109+
- Uvicorn（ASGIサーバー）
- Jinja2（テンプレートエンジン）
- uv（パッケージマネージャー）

## プロジェクト構成

```
mock/
├── app.py                 # FastAPIアプリケーション
├── templates/             # HTMLテンプレート
│   ├── index.html
│   ├── main.html
│   └── results.html
├── static/                # CSS/JS/画像
│   └── style.css
├── requirements.txt       # 依存関係
└── README.md             # 起動方法
```

## 基本的な実装

### app.py

```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# 静的ファイルとテンプレートの設定
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """ランディングページ"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/main", response_class=HTMLResponse)
async def main_feature(request: Request):
    """メイン機能ページ"""
    return templates.TemplateResponse("main.html", {"request": request})

@app.post("/api/process")
async def process(data: dict):
    """処理API（ダミー）"""
    return {
        "status": "success",
        "result": f"処理結果: {data.get('input', '')}"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### templates/index.html

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>サービス名</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <header>
        <h1>🚀 サービス名</h1>
    </header>
    
    <main>
        <section>
            <h2>サービス概要</h2>
            <p>ここにサービスの説明を記載します。</p>
        </section>
        
        <section>
            <h2>主要機能</h2>
            <div class="feature-grid">
                <div class="feature">
                    <h3>機能1</h3>
                    <p>機能1の説明</p>
                </div>
                <div class="feature">
                    <h3>機能2</h3>
                    <p>機能2の説明</p>
                </div>
                <div class="feature">
                    <h3>機能3</h3>
                    <p>機能3の説明</p>
                </div>
            </div>
        </section>
        
        <section>
            <a href="/main" class="button">体験する</a>
        </section>
    </main>
</body>
</html>
```

### static/style.css

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: sans-serif;
    line-height: 1.6;
    color: #333;
}

header {
    background: #0066cc;
    color: white;
    padding: 1rem 2rem;
}

main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

section {
    margin: 2rem 0;
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}

.feature {
    padding: 1.5rem;
    border: 1px solid #ddd;
    border-radius: 8px;
}

.button {
    display: inline-block;
    padding: 1rem 2rem;
    background: #0066cc;
    color: white;
    text-decoration: none;
    border-radius: 4px;
}
```

## 起動方法

### 1. 仮想環境の作成

```bash
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 2. 依存関係のインストール

```bash
uv pip install -r requirements.txt
```

### 3. アプリケーションの起動

```bash
python app.py
```

### 4. ブラウザで開く

http://localhost:8000

## API実装

### GETエンドポイント

```python
@app.get("/api/data")
async def get_data():
    return {"data": ["item1", "item2", "item3"]}
```

### POSTエンドポイント

```python
from pydantic import BaseModel

class InputData(BaseModel):
    text: str
    value: int

@app.post("/api/submit")
async def submit_data(data: InputData):
    return {"received": data.text, "value": data.value}
```

### フォームデータの受信

```python
from fastapi import Form

@app.post("/api/form")
async def handle_form(
    name: str = Form(...),
    email: str = Form(...)
):
    return {"name": name, "email": email}
```

## JavaScriptでのAPI呼び出し

```javascript
// POSTリクエスト
async function submitData() {
    const response = await fetch('/api/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            input: 'データ'
        })
    });
    
    const data = await response.json();
    console.log(data);
}

// GETリクエスト
async function getData() {
    const response = await fetch('/api/data');
    const data = await response.json();
    console.log(data);
}
```

## Tips

### CORS設定（必要な場合）

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 自動リロード（開発時）

```bash
uvicorn app:app --reload --port 8000
```

## トラブルシューティング

### ポートが使用中

```bash
# 別のポートで起動
python app.py  # app.py内でポート番号を変更
# または
uvicorn app:app --port 8001
```

### テンプレートが見つからない

- `templates/` ディレクトリが存在するか確認
- ファイル名が正しいか確認

## 参考リンク

- [FastAPI公式ドキュメント](https://fastapi.tiangolo.com/)
- [Jinja2ドキュメント](https://jinja.palletsprojects.com/)
