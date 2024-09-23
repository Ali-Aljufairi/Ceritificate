import os
from pathlib import Path
import requests
from PIL import Image

DEFAULT_FONT_URL = "https://github.com/google/fonts/raw/main/apache/roboto/Roboto-Regular.ttf"
DEFAULT_FONT_NAME = "Roboto-Regular.ttf"


def ensure_directories_exist(directories):
    """Ensure required directories exist, create them if not."""
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def download_default_font():
    """Download the default Roboto font if no fonts are available."""
    font_path = Path("font") / DEFAULT_FONT_NAME
    print(f"No fonts found, downloading default font: {DEFAULT_FONT_NAME}...")
    try:
        response = requests.get(DEFAULT_FONT_URL)
        font_path.write_bytes(response.content)
        print(f"Font downloaded and saved to {font_path}")
    except Exception as e:
        print(f"Failed to download font: {e}")
        exit(1)


def create_default_white_certificate():
    """Create a default white certificate image if no templates are found."""
    cert_path = Path("cert") / "default_white_cert.png"
    print("No certificate templates found, generating a white background certificate...")
    try:
        img = Image.new("RGB", (800, 600), color="white")  # Default size 800x600
        img.save(cert_path)
        print(f"White background certificate generated and saved to {cert_path}")
    except Exception as e:
        print(f"Failed to create a white background certificate: {e}")
        exit(1)


def list_files_in_directory(directory, extension=None):
    """List files in the specified directory, filter by extension if provided."""
    path = Path(directory)
    if extension:
        return [file.name for file in path.glob(f"*{extension}")]
    return [file.name for file in path.iterdir() if file.is_file()]