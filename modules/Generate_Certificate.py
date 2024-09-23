from PIL import Image, ImageFont, ImageDraw


def Generate_Certificate(
    
    data: list,
    certificate: str,
    font_path_name: str,
    color: tuple,
    Name_position: int,
    font_size_name: int,
    project_font: str,
    project_font_size: int,
    project_position: int,
    
) -> None:
    for name in data:
        Name_position = Name_position
        

        img = Image.open(certificate, mode="r")

        image_width = img.width

        image_height = img.height

        draw = ImageDraw.Draw(img)

        Namefont = ImageFont.truetype(
            font_path_name,
            font_size_name,
            )

        # projectfont = ImageFont.truetype(
            # project_font,
            # project_font_size,
        # )
        draw.text(
            (
                (image_width - draw.textlength(name, font=Namefont)) / 2,
                Name_position,
            ),
            name,
            color,
            font=Namefont,
        )
        
        # draw.text(
            # (
                # (image_width - draw.textlength(project, font=projectfont)) / 2,
                # project_position,
            # ),
            # project,
            # color,
            # font= projectfont,
        # )

        img.save("Genrated Certificates/{}.png".format(name))
