#!/usr/bin/env python3
"""
プレゼン資料自動生成スクリプト

ideationフォルダの成果物を読み込み、
Strands Agentsを使ってプレゼン用に整形し、
HTML形式のプレゼン資料を生成します。
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from strands import Agent

# .envファイルを読み込み
load_dotenv()

# 固定モデル（高精度モデルを使用）
BEDROCK_MODEL = "global.anthropic.claude-sonnet-4-5-20250929-v1:0"

# パスの設定
SCRIPT_DIR = Path(__file__).parent
YOUR_WORK_DIR = SCRIPT_DIR.parent
IDEATION_DIR = YOUR_WORK_DIR / "ideation"
OUTPUT_HTML = SCRIPT_DIR / "index.html"

# 成果物ファイル
PERSONA_FILE = IDEATION_DIR / "step1_persona.md"
IDEAS_FILE = IDEATION_DIR / "step2_ideas.md"
PRFAQ_FILE = IDEATION_DIR / "step3_prfaq.md"


def select_design_theme() -> dict:
    """デザインテーマをインタラクティブに選択"""
    
    print("\n" + "=" * 60)
    print("🎨 デザインを選択してください")
    print("=" * 60 + "\n")
    
    # 質問1: カラーテーマ
    print("[1/6] カラーテーマを選んでください:")
    print("  1. パープル・グラデーション (知的・落ち着き) [デフォルト]")
    print("  2. ブルー・グリーン (爽やか・テック系)")
    print("  3. オレンジ・ピンク (温かみ・消費者向け)")
    print("  4. ダーク・モード (クール・スタイリッシュ)")
    color_theme = input("選択 (1-4, Enter=1): ").strip() or "1"
    
    # 質問2: 雰囲気
    print("\n[2/6] 雰囲気を選んでください:")
    print("  1. ビジネス・フォーマル [デフォルト]")
    print("  2. フレンドリー・カジュアル")
    print("  3. テック・イノベーション")
    tone = input("選択 (1-3, Enter=1): ").strip() or "1"
    
    # 質問3: アニメーション
    print("\n[3/6] アニメーションを選んでください:")
    print("  1. 控えめ")
    print("  2. 標準 [デフォルト]")
    print("  3. ダイナミック")
    animation = input("選択 (1-3, Enter=2): ").strip() or "2"
    
    # 質問4: 自由記述
    print("\n[4/6] その他、こだわりたいポイントがあれば教えてください:")
    print("  例: 「ポップな印象にしたい」「文字を大きめに」「シンプルに」")
    print("  ※ 改行なしで1行で入力してください。なければEnterでスキップ")
    custom_request = input("要望: ").strip()
    
    # 質問5: チームメンバー募集（ポジション・スキル）
    print("\n[5/6] 募集したいポジション・スキルを選んでください（複数選択可、カンマ区切り）:")
    print("  1. フロントエンドエンジニア")
    print("  2. バックエンドエンジニア")
    print("  3. インフラ・DevOpsエンジニア")
    print("  4. UI/UXデザイナー")
    print("  5. ビジネス・マーケティング")
    print("  6. データサイエンティスト")
    print("  7. その他")
    print("  例: 1,3,5 または Enter でスキップ")
    positions_input = input("選択: ").strip()
    
    # ポジション選択を処理
    position_map = {
        "1": "フロントエンドエンジニア",
        "2": "バックエンドエンジニア",
        "3": "インフラ・DevOpsエンジニア",
        "4": "UI/UXデザイナー",
        "5": "ビジネス・マーケティング",
        "6": "データサイエンティスト",
        "7": "その他"
    }
    
    selected_positions = []
    if positions_input:
        for num in positions_input.split(","):
            num = num.strip()
            if num in position_map:
                selected_positions.append(position_map[num])
    
    # "その他"が選ばれた場合は追加入力
    if "その他" in selected_positions:
        print("\n  「その他」の具体的なポジション・スキルを入力してください:")
        other_position = input("  ポジション: ").strip()
        if other_position:
            selected_positions.remove("その他")
            selected_positions.append(other_position)
        else:
            selected_positions.remove("その他")
    
    # 質問6: 価値観・考え方
    print("\n[6/6] どんな考え方・価値観を持った人と組みたいですか？")
    print("  例: 「ユーザー視点を大切にする人」「失敗を恐れずチャレンジする人」")
    print("  ※ 1行で入力、なければEnterでスキップ")
    values = input("価値観: ").strip()
    
    print("\n✅ 設定完了！プレゼンを生成中...\n")
    
    return {
        "color_theme": color_theme,
        "tone": tone,
        "animation": animation,
        "custom_request": custom_request,
        "team_positions": selected_positions,
        "team_values": values
    }


def get_theme_config(design_settings: dict) -> dict:
    """デザイン設定からテーマ設定を生成"""
    
    # カラーテーマのマッピング
    color_themes = {
        "1": {
            "name": "パープル・グラデーション",
            "primary_gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            "section_gradients": [
                "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
                "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
                "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
                "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
                "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
            ],
            "accent_colors": ["#667eea", "#f5576c", "#4facfe", "#fa709a"]
        },
        "2": {
            "name": "ブルー・グリーン",
            "primary_gradient": "linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%)",
            "section_gradients": [
                "linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%)",
                "linear-gradient(135deg, #2af598 0%, #009efd 100%)",
                "linear-gradient(135deg, #08aeea 0%, #2af598 100%)",
                "linear-gradient(135deg, #00b4db 0%, #0083b0 100%)",
                "linear-gradient(135deg, #38ef7d 0%, #11998e 100%)",
                "linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%)"
            ],
            "accent_colors": ["#00d2ff", "#2af598", "#08aeea", "#38ef7d"]
        },
        "3": {
            "name": "オレンジ・ピンク",
            "primary_gradient": "linear-gradient(135deg, #ff6a00 0%, #ee0979 100%)",
            "section_gradients": [
                "linear-gradient(135deg, #ff6a00 0%, #ee0979 100%)",
                "linear-gradient(135deg, #ff9a56 0%, #ff6a00 100%)",
                "linear-gradient(135deg, #f953c6 0%, #b91d73 100%)",
                "linear-gradient(135deg, #ffa751 0%, #ffe259 100%)",
                "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
                "linear-gradient(135deg, #ff6a00 0%, #ee0979 100%)"
            ],
            "accent_colors": ["#ff6a00", "#ff9a56", "#f953c6", "#ffa751"]
        },
        "4": {
            "name": "ダーク・モード",
            "primary_gradient": "linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)",
            "section_gradients": [
                "linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)",
                "linear-gradient(135deg, #0f3460 0%, #16213e 100%)",
                "linear-gradient(135deg, #16213e 0%, #0f3460 100%)",
                "linear-gradient(135deg, #1a1a2e 0%, #0f3460 100%)",
                "linear-gradient(135deg, #16213e 0%, #533483 100%)",
                "linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)"
            ],
            "accent_colors": ["#e94560", "#0f3460", "#533483", "#e94560"]
        }
    }
    
    # 雰囲気のマッピング
    tone_descriptions = {
        "1": "ビジネス・フォーマル",
        "2": "フレンドリー・カジュアル",
        "3": "テック・イノベーション"
    }
    
    # アニメーションのマッピング
    animation_levels = {
        "1": "控えめ",
        "2": "標準",
        "3": "ダイナミック"
    }
    
    return {
        "color_config": color_themes.get(design_settings["color_theme"], color_themes["1"]),
        "tone_description": tone_descriptions.get(design_settings["tone"], tone_descriptions["1"]),
        "animation_level": animation_levels.get(design_settings["animation"], animation_levels["2"]),
        "custom_request": design_settings["custom_request"],
        "team_positions": design_settings.get("team_positions", []),
        "team_values": design_settings.get("team_values", "")
    }


def read_file(file_path: Path) -> str:
    """ファイルを読み込む"""
    if not file_path.exists():
        print(f"⚠️  警告: {file_path.name} が見つかりません")
        return ""
    
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def extract_content_with_ai(persona: str, ideas: str, prfaq: str, theme_config: dict) -> dict:
    """
    Strands Agentsを使って、プレゼン用に内容を抽出・整形
    """
    print("🤖 AIがプレゼン資料を作成中...")
    
    # カスタム要望のサニタイズ
    # ユーザー入力をそのまま使うのではなく、文字列連結で安全に処理
    custom_request_safe = theme_config["custom_request"]
    team_positions = theme_config.get("team_positions", [])
    team_values = theme_config.get("team_values", "")
    
    # システムプロンプトを文字列連結で構築（f-stringの入れ子を避ける）
    design_info = f"""【デザイン設定】
- カラーテーマ: {theme_config['color_config']['name']}
- 雰囲気: {theme_config['tone_description']}
- アニメーション: {theme_config['animation_level']}"""
    
    # カスタム要望がある場合は追加（文字列連結で安全に）
    if custom_request_safe:
        design_info += "\n- カスタム要望: " + custom_request_safe
    
    # チームメンバー募集情報を追加
    team_info = "\n\n【チームメンバー募集情報】"
    if team_positions:
        team_info += "\n- 募集ポジション: " + "、".join(team_positions)
    if team_values:
        team_info += "\n- 求める価値観: " + team_values
    
    agent = Agent(
        model=BEDROCK_MODEL,
        system_prompt=f"""あなたはプレゼンテーション資料作成の専門家です。
        
{design_info}{team_info}

与えられたアイディアソンの成果物から、上記のデザイン設定に合った観衆の目を引く魅力的なプレゼン資料の内容を抽出してください。

以下のJSON形式で出力してください（JSON以外の説明は不要）：

{{
  "service_name": "サービス名",
  "tagline": "キャッチコピー（20文字以内、心に刺さる一言）",
  "problem_title": "課題の見出し（15文字以内）",
  "problem_description": "誰のどんな課題を解決するか（100文字以内、ペルソナと課題を簡潔に）",
  "solution_title": "解決策の見出し（15文字以内）",
  "solution_description": "どう解決するか（150文字以内）",
  "features": [
    {{"title": "機能1タイトル", "description": "説明（50文字以内）"}},
    {{"title": "機能2タイトル", "description": "説明（50文字以内）"}},
    {{"title": "機能3タイトル", "description": "説明（50文字以内）"}}
  ],
  "demo_title": "デモ・モックの見出し",
  "demo_steps": [
    "ステップ1の説明（30文字以内）",
    "ステップ2の説明（30文字以内）",
    "ステップ3の説明（30文字以内）"
  ],
  "strengths": [
    {{"title": "強み1", "description": "説明（50文字以内）"}},
    {{"title": "強み2", "description": "説明（50文字以内）"}},
    {{"title": "強み3", "description": "説明（50文字以内）"}}
  ],
  "team_message": "チームメンバー募集のメッセージ（100文字以内、熱意が伝わる文章）",
  "vision": "実現したい世界（80文字以内、このサービスが目指す未来）"
}}

重要：
- 観衆の目を引く、インパクトのある表現を使う
- 簡潔で分かりやすく
- 数字や具体例を入れる
- 熱量が伝わる表現にする
- team_messageとvisionは、このプロダクト固有の内容にすること（一般的な表現は避ける）
"""
    )
    
    prompt = f"""以下のアイディアソンの成果物から、プレゼン資料用の内容を抽出してください。

# Step1: 顧客理解
{persona}

# Step2: アイディア発明
{ideas}

# Step3: PR/FAQ
{prfaq}

上記の内容を基に、観衆を惹きつけるプレゼン資料の内容を JSON 形式で出力してください。
"""
    
    try:
        result = agent(prompt)
        content = result.message['content'][0]['text']
        
        # JSONを抽出（```json ... ``` で囲まれている場合に対応）
        import json
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        data = json.loads(content)
        return data
        
    except Exception as e:
        print(f"❌ エラー: AI処理に失敗しました - {e}")
        sys.exit(1)


def generate_html(content: dict, theme_config: dict) -> str:
    """
    HTMLプレゼン資料を生成
    モダンでビジュアルが美しいLP風のデザイン
    """
    
    # テーマ設定を取得
    color_config = theme_config["color_config"]
    animation_level = theme_config["animation_level"]
    
    # アニメーション速度の設定
    animation_speed = {
        "控えめ": "1.2s",
        "標準": "0.6s",
        "ダイナミック": "0.4s"
    }.get(animation_level, "0.6s")
    
    # セクションごとのグラデーション
    section_gradients = color_config["section_gradients"]
    accent_colors = color_config["accent_colors"]
    
    # 機能セクションのHTML生成
    features_html = ""
    for i, feature in enumerate(content.get("features", []), 1):
        features_html += f"""
        <div class="feature-card" style="animation-delay: {i * 0.1}s">
          <div class="feature-number">{i}</div>
          <h3>{feature['title']}</h3>
          <p>{feature['description']}</p>
        </div>
"""
    
    # デモステップのHTML生成
    demo_steps_html = ""
    for i, step in enumerate(content.get("demo_steps", []), 1):
        demo_steps_html += f"""
        <div class="demo-step">
          <div class="step-number">Step {i}</div>
          <p>{step}</p>
        </div>
"""
    
    # 強みセクションのHTML生成
    strengths_html = ""
    for strength in content.get("strengths", []):
        strengths_html += f"""
        <div class="strength-card">
          <h3>✨ {strength['title']}</h3>
          <p>{strength['description']}</p>
        </div>
"""
    
    # チームメンバー募集セクションのHTML生成
    team_positions = theme_config.get("team_positions", [])
    team_values = theme_config.get("team_values", "")
    
    # ポジション別のアイコンマッピング
    position_icons = {
        "フロントエンドエンジニア": "👨‍💻",
        "バックエンドエンジニア": "⚙️",
        "インフラ・DevOpsエンジニア": "🛠️",
        "UI/UXデザイナー": "🎨",
        "ビジネス・マーケティング": "📊",
        "データサイエンティスト": "📈"
    }
    
    # 募集ポジションのHTML
    positions_html = ""
    if team_positions:
        positions_html = '<div class="team-positions">'
        for position in team_positions:
            icon = position_icons.get(position, "✨")
            positions_html += f'<div class="position-tag">{icon} {position}</div>\n'
        positions_html += '</div>'
    
    # 求める価値観のHTML
    values_html = ""
    if team_values:
        # カンマまたは「、」で分割
        values_list = [v.strip() for v in team_values.replace("、", ",").split(",") if v.strip()]
        if values_list:
            values_html = '<div class="team-values">'
            for value in values_list:
                values_html += f'<div class="value-item">✨ {value}</div>\n'
            values_html += '</div>'
    
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{content.get('service_name', 'プレゼンテーション')}</title>
  <style>
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}
    
    body {{
      font-family: 'Helvetica Neue', Arial, 'Hiragino Kaku Gothic ProN', 'Hiragino Sans', Meiryo, sans-serif;
      line-height: 1.8;
      color: #333;
      background: {section_gradients[0]};
      overflow-x: hidden;
    }}
    
    .section {{
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 60px 20px;
      scroll-snap-align: start;
    }}
    
    .container {{
      max-width: 1200px;
      margin: 0 auto;
      background: rgba(255, 255, 255, 0.98);
      padding: 80px 60px;
      border-radius: 30px;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
      backdrop-filter: blur(10px);
    }}
    
    /* タイトルセクション */
    #hero {{
      background: {section_gradients[0]};
    }}
    
    #hero .container {{
      background: transparent;
      box-shadow: none;
      text-align: center;
      color: white;
    }}
    
    h1 {{
      font-size: 4rem;
      font-weight: 900;
      margin-bottom: 20px;
      background: linear-gradient(135deg, #fff 0%, #f0f0f0 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: fadeInUp 1s ease-out;
    }}
    
    .tagline {{
      font-size: 1.8rem;
      margin-bottom: 40px;
      opacity: 0.95;
      animation: fadeInUp 1s ease-out 0.2s both;
    }}
    
    /* 課題セクション */
    #problem {{
      background: {section_gradients[1]};
    }}
    
    .section-title {{
      font-size: 2.5rem;
      margin-bottom: 30px;
      color: {accent_colors[0]};
      border-bottom: 4px solid {accent_colors[0]};
      padding-bottom: 15px;
      display: inline-block;
    }}
    
    #problem .section-title {{
      color: {accent_colors[1]};
      border-color: {accent_colors[1]};
    }}
    
    #solution .section-title {{
      color: {accent_colors[2]};
      border-color: {accent_colors[2]};
    }}
    
    .large-text {{
      font-size: 1.5rem;
      line-height: 2;
      color: #444;
      margin-top: 20px;
    }}
    
    /* 機能カード */
    .features-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 30px;
      margin-top: 40px;
    }}
    
    .feature-card {{
      background: {section_gradients[2]};
      padding: 40px 30px;
      border-radius: 20px;
      color: white;
      text-align: center;
      transform: translateY(0);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      animation: fadeInUp {animation_speed} ease-out both;
    }}
    
    .feature-card:hover {{
      transform: translateY(-10px);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    }}
    
    .feature-number {{
      font-size: 3rem;
      font-weight: 900;
      margin-bottom: 15px;
      opacity: 0.3;
    }}
    
    .feature-card h3 {{
      font-size: 1.5rem;
      margin-bottom: 15px;
    }}
    
    .feature-card p {{
      font-size: 1.1rem;
      opacity: 0.9;
    }}
    
    /* デモセクション */
    #demo {{
      background: {section_gradients[3]};
    }}
    
    .demo-steps {{
      display: flex;
      flex-direction: column;
      gap: 30px;
      margin-top: 40px;
    }}
    
    .demo-step {{
      background: {section_gradients[2]};
      padding: 30px 40px;
      border-radius: 15px;
      color: white;
      display: flex;
      align-items: center;
      gap: 30px;
      animation: fadeInLeft {animation_speed} ease-out both;
    }}
    
    .step-number {{
      font-size: 2rem;
      font-weight: 900;
      background: rgba(255, 255, 255, 0.2);
      padding: 10px 25px;
      border-radius: 10px;
      min-width: 140px;
      text-align: center;
    }}
    
    .demo-step p {{
      font-size: 1.3rem;
      flex: 1;
    }}
    
    /* 強みセクション */
    #strengths {{
      background: {section_gradients[4]};
    }}
    
    .strengths-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 30px;
      margin-top: 40px;
    }}
    
    .strength-card {{
      background: white;
      padding: 40px 30px;
      border-radius: 20px;
      border-left: 6px solid {accent_colors[3]};
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease;
      animation: fadeInUp {animation_speed} ease-out both;
    }}
    
    .strength-card:hover {{
      transform: translateY(-5px);
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
    }}
    
    .strength-card h3 {{
      font-size: 1.5rem;
      margin-bottom: 15px;
      color: {accent_colors[3]};
    }}
    
    .strength-card p {{
      font-size: 1.1rem;
      color: #666;
    }}
    
    /* チーム募集セクション */
    #team {{
      background: {section_gradients[5]};
    }}
    
    #team .container {{
      background: transparent;
      text-align: center;
      color: white;
    }}
    
    #team h2 {{
      font-size: 3rem;
      margin-bottom: 30px;
      color: white;
    }}
    
    .team-section-title {{
      font-size: 2rem;
      margin-top: 40px;
      margin-bottom: 25px;
      color: white;
      font-weight: 600;
    }}
    
    .team-positions {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 20px;
      margin: 30px 0;
    }}
    
    .position-tag {{
      background: rgba(255, 255, 255, 0.2);
      backdrop-filter: blur(10px);
      padding: 15px 30px;
      border-radius: 50px;
      font-size: 1.3rem;
      font-weight: 600;
      border: 2px solid rgba(255, 255, 255, 0.3);
      transition: all 0.3s ease;
      animation: fadeInUp {animation_speed} ease-out both;
    }}
    
    .position-tag:hover {{
      background: rgba(255, 255, 255, 0.3);
      transform: translateY(-5px);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }}
    
    .team-values {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 15px;
      margin: 30px 0;
    }}
    
    .value-item {{
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(10px);
      padding: 12px 35px;
      border-radius: 15px;
      font-size: 1.3rem;
      border: 2px solid rgba(255, 255, 255, 0.25);
      max-width: 600px;
      animation: fadeInLeft {animation_speed} ease-out both;
    }}
    
    .team-message {{
      font-size: 1.8rem;
      line-height: 2;
      margin: 40px 0;
      opacity: 0.95;
    }}
    
    .vision {{
      font-size: 2.2rem;
      font-weight: 700;
      margin-top: 50px;
      padding: 40px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 20px;
      border: 3px solid rgba(255, 255, 255, 0.3);
    }}
    
    /* アニメーション */
    @keyframes fadeInUp {{
      from {{
        opacity: 0;
        transform: translateY(30px);
      }}
      to {{
        opacity: 1;
        transform: translateY(0);
      }}
    }}
    
    @keyframes fadeInLeft {{
      from {{
        opacity: 0;
        transform: translateX(-30px);
      }}
      to {{
        opacity: 1;
        transform: translateX(0);
      }}
    }}
    
    /* レスポンシブ */
    @media (max-width: 768px) {{
      h1 {{
        font-size: 2.5rem;
      }}
      
      .tagline {{
        font-size: 1.3rem;
      }}
      
      .section-title {{
        font-size: 2rem;
      }}
      
      .container {{
        padding: 40px 30px;
      }}
      
      .demo-step {{
        flex-direction: column;
        text-align: center;
      }}
      
      .feature-card, .strength-card {{
        padding: 30px 20px;
      }}
      
      .position-tag {{
        font-size: 1.1rem;
        padding: 12px 20px;
      }}
      
      .value-item {{
        font-size: 1.1rem;
        padding: 10px 25px;
      }}
      
      .team-message {{
        font-size: 1.4rem;
      }}
      
      .vision {{
        font-size: 1.6rem;
        padding: 30px 20px;
      }}
    }}
    
    /* スクロールヒント */
    .scroll-hint {{
      position: absolute;
      bottom: 40px;
      left: 50%;
      transform: translateX(-50%);
      color: white;
      font-size: 1rem;
      animation: bounce 2s infinite;
    }}
    
    @keyframes bounce {{
      0%, 20%, 50%, 80%, 100% {{
        transform: translateX(-50%) translateY(0);
      }}
      40% {{
        transform: translateX(-50%) translateY(-10px);
      }}
      60% {{
        transform: translateX(-50%) translateY(-5px);
      }}
    }}
  </style>
</head>
<body>
  <!-- 1. タイトル -->
  <section id="hero" class="section">
    <div class="container">
      <h1>{content.get('service_name', 'サービス名')}</h1>
      <p class="tagline">{content.get('tagline', 'キャッチコピー')}</p>
      <div class="scroll-hint">▼ Scroll Down</div>
    </div>
  </section>

  <!-- 2. 課題 -->
  <section id="problem" class="section">
    <div class="container">
      <h2 class="section-title">{content.get('problem_title', '解決する課題')}</h2>
      <p class="large-text">{content.get('problem_description', '課題の説明')}</p>
    </div>
  </section>

  <!-- 3. 解決策 -->
  <section id="solution" class="section">
    <div class="container">
      <h2 class="section-title">{content.get('solution_title', '私たちの解決策')}</h2>
      <p class="large-text">{content.get('solution_description', '解決策の説明')}</p>
      <div class="features-grid">
{features_html}
      </div>
    </div>
  </section>

  <!-- 4. デモ・モック -->
  <section id="demo" class="section">
    <div class="container">
      <h2 class="section-title">{content.get('demo_title', '使い方')}</h2>
      <div class="demo-steps">
{demo_steps_html}
      </div>
    </div>
  </section>

  <!-- 5. 独自の強み -->
  <section id="strengths" class="section">
    <div class="container">
      <h2 class="section-title">独自の強み</h2>
      <div class="strengths-grid">
{strengths_html}
      </div>
    </div>
  </section>

  <!-- 6. チーム募集 -->
  <section id="team" class="section">
    <div class="container">
      <h2>🎉 一緒にやりませんか？</h2>
      {f'<h3 class="team-section-title">募集しているメンバー</h3>{positions_html}' if positions_html else ''}
      {f'<h3 class="team-section-title">こんな人と組みたい</h3>{values_html}' if values_html else ''}
      <p class="team-message">{content.get('team_message', 'チームメンバーを募集しています！')}</p>
      <div class="vision">
        {content.get('vision', '実現したい世界')}
      </div>
    </div>
  </section>

  <script>
    // スムーススクロール
    document.addEventListener('DOMContentLoaded', function() {{
      // セクションが表示されたらアニメーション
      const observer = new IntersectionObserver((entries) => {{
        entries.forEach(entry => {{
          if (entry.isIntersecting) {{
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
          }}
        }});
      }}, {{ threshold: 0.1 }});

      document.querySelectorAll('.section').forEach(section => {{
        section.style.opacity = '0';
        section.style.transform = 'translateY(50px)';
        section.style.transition = 'opacity {animation_speed} ease, transform {animation_speed} ease';
        observer.observe(section);
      }});
    }});
  </script>
</body>
</html>
"""
    
    return html


def main():
    print("=" * 60)
    print("🎨 プレゼンテーション資料 自動生成ツール")
    print("=" * 60)
    print()
    
    # デザイン選択
    design_settings = select_design_theme()
    theme_config = get_theme_config(design_settings)
    
    # ファイルの存在確認
    print("📂 成果物を読み込み中...")
    persona = read_file(PERSONA_FILE)
    ideas = read_file(IDEAS_FILE)
    prfaq = read_file(PRFAQ_FILE)
    
    if not persona or not ideas or not prfaq:
        print()
        print("❌ エラー: 成果物ファイルが不足しています")
        print(f"   以下のファイルが必要です：")
        print(f"   - {PERSONA_FILE}")
        print(f"   - {IDEAS_FILE}")
        print(f"   - {PRFAQ_FILE}")
        print()
        print("   Step1-3を完了してから、再度実行してください。")
        sys.exit(1)
    
    print("✅ 成果物の読み込み完了")
    print()
    
    # AIで内容を抽出・整形
    content = extract_content_with_ai(persona, ideas, prfaq, theme_config)
    print("✅ AI処理完了")
    print()
    
    # HTML生成
    print("📝 HTMLプレゼン資料を生成中...")
    html = generate_html(content, theme_config)
    
    # ファイル保存
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"✅ 保存完了: {OUTPUT_HTML}")
    print()
    print("=" * 60)
    print("🎉 プレゼン資料の作成が完了しました！")
    print("=" * 60)
    print()
    print(f"📍 ファイルの場所: {OUTPUT_HTML}")
    print()
    print("📖 確認方法:")
    print(f"   ブラウザで {OUTPUT_HTML} を開いてください")
    print()
    print("💡 Tips:")
    print("   - スクロールして全6セクションを確認")
    print("   - 気になる部分は index.html を直接編集してもOK")
    print("   - 画面幅を変えてレスポンシブデザインも確認してみましょう")
    print()


if __name__ == "__main__":
    main()

