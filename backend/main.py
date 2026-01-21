from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from services.openai_service import gerar_versiculos
from services.template_service import gerar_word_com_template

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TemaRequest(BaseModel):
    tema: str

@app.post("/gerar")
async def gerar(request: TemaRequest):
    tema = request.tema

    if not tema:
        raise HTTPException(status_code=400, detail="Tema não pode ser vazio")

    try:
        versiculos = gerar_versiculos(tema)
        caminho_pdf = gerar_word_com_template(versiculos)
        return FileResponse(caminho_pdf, media_type="application/pdf", filename="versiculos.pdf")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
