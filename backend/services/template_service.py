from docx import Document
import tempfile

def gerar_word_com_template(dados, template_path):
    doc = Document(template_path)

    for i, item in enumerate(dados, start=1):
        placeholder = f"{{{{V{i}}}}}"
        texto = f'{item["texto"]}\n({item["endereco"]})'

        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    if placeholder in cell.text:
                        cell.text = cell.text.replace(placeholder, texto)

    output = tempfile.mktemp(suffix=".docx")
    doc.save(output)
    return output

