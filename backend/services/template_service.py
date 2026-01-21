from docx import Document
from docx.shared import Inches
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.shared import Pt
from fpdf import FPDF
import tempfile

def gerar_word_com_template(versiculos):
    # cria documento Word
    doc = Document()
    table = doc.add_table(rows=3, cols=4)
    table.style = 'Light List'

    idx = 0
    for i in range(3):
        for j in range(4):
            if idx < len(versiculos):
                cell = table.cell(i, j)
                cell.text = f"{versiculos[idx]['texto']} ({versiculos[idx]['endereco']})"
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                for paragraph in cell.paragraphs:
                    paragraph.alignment = 1  # center
                    for run in paragraph.runs:
                        run.font.size = Pt(10)
                idx += 1

    tmp_word = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
    doc.save(tmp_word.name)

    # opcional: gerar PDF direto com fpdf
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for v in versiculos:
        pdf.multi_cell(0, 10, f"{v['texto']} ({v['endereco']})")
    tmp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(tmp_pdf.name)

    return tmp_pdf.name
