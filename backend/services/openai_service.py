import os
import json
from openai import OpenAI

# Inicializa cliente OpenAI usando variável de ambiente
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
    """
    Recebe um tema, consulta o GPT e retorna lista de versículos:
    [
        {"texto": "...", "endereco": "..."},
        ...
    ]
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": PROMPT.format(tema=tema)}],
            temperature=0.3
        )
        conteudo = response.choices[0].message.content
        return json.loads(conteudo)
    except json.JSONDecodeError:
        raise Exception("GPT retornou JSON inválido")
    except Exception as e:
        raise Exception(f"Erro ao gerar versículos: {str(e)}")
