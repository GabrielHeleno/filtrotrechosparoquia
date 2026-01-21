from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
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

class Tema(BaseModel):
    tema: str

@app.post("/gerar")
def gerar(t: Tema):
    try:
        dados = gerar_versiculos(t.tema)
        word_path = gerar_word_com_template(dados, "template.docx")

        return FileResponse(
            word_path,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            filename="versiculos.docx"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

