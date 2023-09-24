from modules.Generate_Certificate import Generate_Certificate
from modules.Convertpdf import Convert_pdf
import modules.data_clean as data_clean


def main():
    NAMES = data_clean.Oraginze_data("Names.csv")
    # COLOR = input("Enter the color: ").lstrip("#")
    COLOR = "343434"
    rcolor = tuple(int(COLOR[i : i + 2], 16) for i in (0, 2, 4))

    # text_y_position = int(input("Enter the text y position: "))
    font_size = 100
    text_y_position = 620
    # font_size = int(input("Enter the font size: "))

    Project_Font = "Font\Antic.ttf" 
    Project_Font_Size = 50
    Projepct_Position = 820
    Name_Font = "Font\Playfair.ttf"
    CERTIFICATE = "cert\Ceritifcate.png"

    Generate_Certificate(
        NAMES,
        CERTIFICATE,
        Name_Font,
        rcolor,
        text_y_position,
        font_size,
        Project_Font,
        Project_Font_Size,
        Projepct_Position,
    )
    Convert_pdf(NAMES)


if __name__ == "__main__":
    main()
