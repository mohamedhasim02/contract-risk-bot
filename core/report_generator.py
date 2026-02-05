from fpdf import FPDF
import os

def generate_pdf(summary, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=10)

    for line in summary.split("\n"):
        pdf.multi_cell(0, 8, line)

    pdf.output(filename)
