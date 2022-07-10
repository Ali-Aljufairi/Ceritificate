from PIL import Image, ImageFont, ImageDraw
import img2pdf
import os


def Generate_Certificate(names: list, certificate: str, font_path: str, font_color: tuple, text_y_position: int , font_size: int):
    for name in names:
        text_y_position = text_y_position

        img = Image.open(certificate, mode='r')

        image_width = img.width

        image_height = img.height

        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype(
            font_path,
            font_size,
        )

        # text_width, _ = draw.textsize(name, font=font)

        draw.text(
            (
                (image_width -draw.textlength(name, font=font)) / 2,
                text_y_position,
            ),
            name,
            color,
            font=font)

        img.save("Genrated Certificates/{}.png".format(name))


def Convert_pdf(names: list):
    # convert all files ending in .jpg inside a directory
    dirname = "Genrated Certificates"
    imgs = []
    for fname in os.listdir(dirname):
        if not fname.endswith(".png"):
            continue
        path = os.path.join(dirname, fname)
        if os.path.isdir(path):
            continue
        imgs.append(path)
    for name in names:
        with open("Genrated Certificates/{}.pdf".format(name), "wb") as f:
            f.write(img2pdf.convert(imgs))


if __name__ == "__main__":
    with open("Names.txt") as file:
        NAMES = file.readlines()
        NAMES = [name.strip() for name in NAMES]
        NAMES.pop(-1)
        NAMES.sort()

    text_y_position = 500
    color = (99, 176, 203)
    FONT = "Font/Arvo-Regular.ttf"
    FONT_SIZE = 100
    CERTIFICATE = "Sample Certificate/Certifccate.png"

    Generate_Certificate(NAMES, CERTIFICATE, FONT, color, text_y_position, FONT_SIZE)

#
#     dirname = "Genrated Certificates"
#     imgs = []
#     for fname in os.listdir(dirname):
#         if not fname.endswith(".png"):
#             continue
#         path = os.path.join(dirname, fname)
#         if os.path.isdir(path):
#             continue
#         imgs.append(path)
#
# for name in imgs:
#     with open("Genrated Certificates/{}.pdf".format(name), "wb") as f:
#         f.write(img2pdf.convert(imgs))
#
#
