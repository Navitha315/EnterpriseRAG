from loaders.text_loader import load_text
from loaders.docx_loader import load_docx
from loaders.pdf_loader import load_pdf
from loaders.excel_loader import load_excel

def load_document(path):

    ext = path.split(".")[-1].lower()

    if ext == "txt":
        return load_text(path)

    elif ext == "docx":
        return load_docx(path)

    elif ext == "pdf":
        return load_pdf(path)

    elif ext == "xlsx":
        return load_excel(path)

    else:
        raise Exception(
            f"Unsupported file: {ext}"
        )
