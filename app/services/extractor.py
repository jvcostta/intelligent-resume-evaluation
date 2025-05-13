import pdfplumber

def extract_text(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf: #abre o pdf
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text
