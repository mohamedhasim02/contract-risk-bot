
from fpdf import FPDF
def generate_pdf(summary, filename):
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0,8,summary)
    pdf.output(filename)
