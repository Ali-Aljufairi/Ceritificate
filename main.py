from Generate_Certificate import Generate_Certificate
from Convertpdf import Convert_pdf
import data_clean


def main():
    NAMES = data_clean.Oraginze_data("Names.csv")

    COLOR = input("Enter the color: ").lstrip("#")
    Project_Postion = 820
    font_size_project = 50

    # text_y_position = int(input("Enter the text y position: "))
    # font_size = int(input("Enter the font size: "))

    # good postion and font size for name the certificate
    Name_Postion = 650
    font_size_name = 100
    # COLOR ="1f2428"

    Project_FONT = "Font\Antic.ttf"
    Name_Font = "Font\Playfair.ttf"
    CERTIFICATE = "cert\Ceritifcate.png"
    rcolor = tuple(int(COLOR[i : i + 2], 16) for i in (0, 2, 4))

    Generate_Certificate(
        NAMES,
        CERTIFICATE,
        Name_Font,
        Project_FONT,
        rcolor,
        Name_Postion,
        font_size_name,
        font_size_project,
        Project_Postion
    )
    Convert_pdf(NAMES)


if __name__ == "__main__":
    main()
