
import pdfplumber, docx

def extract_text(file):
    if file.name.endswith(".pdf"):
        text=""
        with pdfplumber.open(file) as pdf:
            for p in pdf.pages:
                text+=p.extract_text()+"\n"
        return text
    if file.name.endswith(".docx"):
        doc=docx.Document(file)
        return "\n".join(p.text for p in doc.paragraphs)
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    return ""
