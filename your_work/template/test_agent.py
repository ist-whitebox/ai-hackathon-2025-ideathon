"""
Strands Agents動作確認用テストスクリプト

使い方:
  cd your_work/template/
  python test_agent.py

前提条件:
  - mock/.envファイルが設定済み
  - mock/.venv/が作成済み
"""
import sys
import os
from pathlib import Path

# mock/.envを読み込むための設定
mock_dir = Path(__file__).parent.parent / "mock"
sys.path.insert(0, str(mock_dir))

from dotenv import load_dotenv
load_dotenv(mock_dir / ".env")

from strands import Agent

def test():
    print("=== Strands Agents動作確認 ===\n")
    
    model_id = os.getenv("AWS_BEDROCK_MODEL_ID")
    print(f"Model ID: {model_id}\n")
    
    agent = Agent(
        model=model_id,
        system_prompt='あなたはテスト用のアシスタントです。'
    )
    
    print("プロンプト送信中...\n")
    
    result = agent('こんにちは')
    
    print(f"✅ レスポンス: {result.message['content'][0]['text']}\n")
    print("=== テスト成功 ===")

if __name__ == "__main__":
    try:
        test()
    except Exception as e:
        print(f"❌ エラー: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
