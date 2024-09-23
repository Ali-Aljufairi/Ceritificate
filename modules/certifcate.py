from PIL import Image, ImageFont, ImageDraw
import os


def generate_certificate(
    data: list,
    certificate: str,
    font_path_name: str,
    color: tuple,
    name_position: int,
    font_size_name: int,
    project_font: str,
    project_font_size: int,
    project_position: int
):
    """Generate certificates for each name in the data list."""
    # Ensure the output directory exists
    os.makedirs("Genrated Certificates", exist_ok=True)

    for name in data:
        img = Image.open(certificate, mode="r")
        image_width = img.width
        draw = ImageDraw.Draw(img)
        Namefont = ImageFont.truetype(font_path_name, font_size_name)

        # Draw the name on the certificate
        draw.text(
            ((image_width - draw.textlength(name, font=Namefont)) / 2, name_position),
            name,
            color,
            font=Namefont,
        )

        img.save(f"Genrated Certificates/{name}.png")