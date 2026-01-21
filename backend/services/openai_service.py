import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("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"))

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
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": PROMPT.format(tema=tema)}],
        temperature=0.3
    )

    return json.loads(response.choices[0].message.content)

