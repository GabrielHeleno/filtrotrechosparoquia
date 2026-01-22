from fpdf import FPDF
import tempfile

def gerar_word_com_template(versiculos):
    """
    Cria um PDF simples com os versículos recebidos e retorna o caminho.
    """
    # Arquivo temporário
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, "Versículos relacionados ao tema", ln=True, align="C")
    pdf.ln(10)

    for v in versiculos:
        texto = v.get("texto", "")
        endereco = v.get("endereco", "")
        linha = f"{texto} ({endereco})"
        pdf.multi_cell(0, 8, linha)
        pdf.ln(2)

    pdf.output(tmp_file.name)
    return tmp_file.name
