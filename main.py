from modules.Generate_Certificate import Generate_Certificate
from modules.Convertpdf import Convert_pdf
import modules.data_clean as data_clean


def main():
    NAMES = data_clean.Oraginze_data("Names.csv")
    COLOR = input("Enter the color: ").lstrip("#")
    rcolor = tuple(int(COLOR[i : i + 2], 16) for i in (0, 2, 4))

    text_y_position = int(input("Enter the text y position: "))
    font_size = int(input("Enter the font size: "))

    Name_Font = "Font\Playfair.ttf"
    CERTIFICATE = "cert\Ceritifcate.png"

    Generate_Certificate(
        NAMES,
        CERTIFICATE,
        Name_Font,
        rcolor,
        text_y_position,
        font_size,
    )
    Convert_pdf(NAMES)


if __name__ == "__main__":
    main()
