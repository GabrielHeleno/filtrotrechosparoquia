from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
import tempfile
import os

from services.openai_service import gerar_versiculos
from services.template_service import gerar_word_com_template

app = FastAPI(title="Filtro de Versículos")

# CORS liberado para qualquer origem (frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo do request
class TemaRequest(BaseModel):
    tema: str

# Rota raiz amigável
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <h1>Backend do Filtro de Versículos</h1>
    <p>Use <a href='/docs'>/docs</a> para testar os endpoints.</p>
    """

# Endpoint de geração do PDF
@app.post("/gerar")
async def gerar_pdf(request: TemaRequest):
    tema = request.tema.strip()
    if not tema:
        raise HTTPException(status_code=400, detail="Tema não pode ser vazio")

    try:
        # Gera os versículos com GPT
        versiculos = gerar_versiculos(tema)

        # Cria PDF temporário
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            caminho_pdf = gerar_word_com_template(versiculos, tmp.name)

        # Retorna PDF
        return FileResponse(caminho_pdf, media_type="application/pdf", filename="versiculos.pdf")

    except Exception as e:
        # Para debug no Render, exibe a mensagem completa do erro
        raise HTTPException(status_code=500, detail=f"Erro ao gerar PDF: {str(e)}")
    finally:
        # Se quiser, pode remover o PDF temporário após envio
        # os.remove(caminho_pdf)
        pass
