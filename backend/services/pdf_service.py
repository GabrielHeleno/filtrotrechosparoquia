from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.pagesizes import A4
import tempfile

def gerar_pdf(dados):
    path = tempfile.mktemp(suffix=".pdf")
    pdf = SimpleDocTemplate(path, pagesize=A4)

    tabela = []
    linha = []

    for i, item in enumerate(dados):
        linha.append(f'{item["texto"]}\n({item["endereco"]})')
        if (i + 1) % 4 == 0:
            tabela.append(linha)
            linha = []

    pdf.build([Table(tabela)])
    return path

