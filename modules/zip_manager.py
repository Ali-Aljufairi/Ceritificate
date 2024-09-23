import os
import shutil
from zipfile import ZipFile


def zip_pdfs(output_filename: str):
    """Zip all PDFs in the 'PDFs/' directory into a single zip file."""
    os.makedirs("zip", exist_ok=True)
    output_path = f"zip/{output_filename}.zip"
    
    with ZipFile(output_path, 'w') as zipf:
        for root, dirs, files in os.walk("PDFs"):
            for file in files:
                if file.endswith(".pdf"):
                    zipf.write(os.path.join(root, file), file)

    print(f"All PDFs have been zipped into {output_path}")


def clean_up_pdfs():
    """Delete all PDFs in the 'PDFs/' directory after they are zipped."""
    for root, dirs, files in os.walk("PDFs"):
        for file in files:
            if file.endswith(".pdf"):
                os.remove(os.path.join(root, file))
    
    print("All generated PDFs have been deleted.")