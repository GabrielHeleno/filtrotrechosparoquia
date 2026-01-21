import os
import json
from openai import OpenAI

PROMPT = """
Selecione exatamente 12 versículos da Bíblia relacionados ao tema: "{tema}"

Retorne APENAS um JSON válido no formato:

[
  {{
    "texto": "Texto do versículo",
    "endereco": "Livro 1,1"
  }}
]
"""

def gerar_versiculos(tema: str):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY não está definida no ambiente")

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": PROMPT.format(tema=tema)}],
        temperature=0.3
    )

    return json.loads(response.choices[0].message.content)
