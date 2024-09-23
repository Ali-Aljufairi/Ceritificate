import img2pdf
import os

def convert_pdf(names: list):
    """Convert generated images to PDFs."""
    os.makedirs("PDFs", exist_ok=True)

    for name in names:
        with open(f"PDFs/{name}.pdf", "wb") as f:
            f.write(img2pdf.convert([f"Genrated Certificates/{name}.png"]))