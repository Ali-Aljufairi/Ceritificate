from PIL import Image, ImageFont, ImageDraw


def Generate_Certificate(
    data: list,
    certificate: str,
    font_path_name: str,
    font_path_project: str,
    color: tuple,
    Name_position: int,
    font_size_name: int,
    font_size_project: int,
    Project_Position: int,
) -> None:
    for name, project in data:
        File_Name = name
        Name_position = Name_position
        Project_Position = Project_Position

        img = Image.open(certificate, mode="r")

        image_width = img.width

        image_height = img.height

        draw = ImageDraw.Draw(img)

        Namefont = ImageFont.truetype(
            font_path_name,
            font_size_name,
        )

        Projectfont = ImageFont.truetype(
            font_path_project,
            font_size_project,
        )
        draw.text(
            (
                (image_width - draw.textlength(name, font=Namefont)) / 2,
                Project_Position,
            ),
            project,
            color,
            font=Projectfont,
        )

        draw.text(
            (
                (image_width - draw.textlength(name, font=Namefont)) / 2,
                Name_position,
            ),
            name,
            color,
            font=Namefont,
        )

        img.save("Genrated Certificates/{}.png".format(name))
