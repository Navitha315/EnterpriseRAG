import fitz

def load_pdf(path):

    text = ""

    doc = fitz.open(path)

    for page in doc:
        text += page.get_text()

    return text
