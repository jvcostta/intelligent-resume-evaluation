import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(
    api_key = os.envirion.get("GROQ_API_KEY"),
    )

def analyze_resume(text: str) -> dict:
    prompt = f"""
    Analise o currículo abaixo e me retorne um resumo contendo:
    - Pontos fortes
    - Pontos fracos
    - Áreas de destaque
    - Pontuação geral de 0 a 100

    Currículo:
    {text}
    """

    response = client.ChatCompletion.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Você é um analista de currículos."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=600
    )

    return {
        "analise": response["choices"][0]["message"]["content"]
    }
