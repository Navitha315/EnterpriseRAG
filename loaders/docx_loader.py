from docx import Document

def load_docx(path):

    doc = Document(path)

    text = "\n".join(
        para.text
        for para in doc.paragraphs
    )

    return text
