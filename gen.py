import google.generativeai as genai



api_key = "AIzaSyDglpOUusSf7PoLJlJdVxPNyqBIn_lydkY"
model_name = "models/gemini-1.5-flash-latest"


def ai(messages):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name=model_name, system_instruction="20대 여성과 같은 챗 형식의 짧은 답변",)
    result = model.generate_content(
        contents=messages,
        request_options={"timeout": 1000},
    )

    return result.text
