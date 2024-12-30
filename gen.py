import google.generativeai as genai
from datetime import datetime

api_key = "AIzaSyDglpOUusSf7PoLJlJdVxPNyqBIn_lydkY"
model_name = "models/gemini-2.0-flash-exp"
system_prompt = f"""**today:** {datetime.now()}

[persona]
- **아빠(개발자) 이름:** "샰롯"
- **내 이름:** "샰롯 봇"
- 20대 여성
- 챗 형식의 짧은 답변
"""


def ai(messages):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name=model_name,
        system_instruction=system_prompt,
    )
    result = model.generate_content(
        contents=messages,
        request_options={"timeout": 1000},
    )

    return result.text.strip()
