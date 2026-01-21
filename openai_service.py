import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("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"))

PROMPT_TEMPLATE = """
Você deve:
1. Considerar toda a Bíblia
2. Selecionar exatamente 12 versículos relacionados ao tema: "{tema}"
3. Retornar APENAS um JSON válido no formato:

[
  {{
    "versiculo": "Texto do versículo",
    "endereco": "Livro 1,1"
  }}
]

Não escreva absolutamente nada fora do JSON.
"""

def gerar_versiculos(tema: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": PROMPT_TEMPLATE.format(tema=tema)}
        ],
        temperature=0.3
    )

    content = response.choices[0].message.content
    return json.loads(content)
