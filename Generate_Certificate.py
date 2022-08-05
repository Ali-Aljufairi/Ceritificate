from PIL import Image, ImageFont, ImageDraw
import img2pdf
import os
def Generate_Certificate(names: list, certificate: str, font_path: str, color:tuple , text_y_position: int , font_size: int):
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



        draw.text(
            (
                (image_width -draw.textlength(name, font=font)) / 2,
                text_y_position,
            ),
            name,
            color ,
            font=font)

        img.save("Genrated Certificates/{}.png".format(name))