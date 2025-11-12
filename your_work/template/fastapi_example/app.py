from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/main", response_class=HTMLResponse)
async def main_feature(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.post("/api/process")
async def process(data: dict):
    return {"status": "success", "result": f"処理結果: {data.get('input', '')}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
