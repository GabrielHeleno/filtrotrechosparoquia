from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
import tempfile

from services.openai_service import gerar_versiculos
from services.template_service import gerar_word_com_template

app = FastAPI(title="Filtro de Versículos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TemaRequest(BaseModel):
    tema: str

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <h1>Backend do Filtro de Versículos</h1>
    <p>Use <a href='/docs'>/docs</a> para testar os endpoints.</p>
    """

@app.post("/gerar")
async def gerar_pdf(request: TemaRequest):
    tema = request.tema.strip()
    if not tema:
        raise HTTPException(status_code=400, detail="Tema não pode ser vazio")

    try:
        versiculos = gerar_versiculos(tema)

        # Cria PDF temporário
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            caminho_pdf = gerar_word_com_template(versiculos, tmp.name)

        return FileResponse(caminho_pdf, media_type="application/pdf", filename="versiculos.pdf")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar PDF: {str(e)}")
