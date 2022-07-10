from PIL import Image, ImageFont, ImageDraw
import img2pdf
import os
def Generate_Certificate(names: list, certificate: str, font_path: str, color: tuple, text_y_position: int):
    for name in names:
        text_y_position = text_y_position

        img = Image.open(certificate, mode='r')

        image_width = img.width

        image_height = img.height

        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype(
            font_path,
            # size=int(image_width / 10),
            100
        )

        text_width, _ = draw.textsize(name, font=font)

        draw.text(
            (

                (image_width - text_width) / 2,
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

