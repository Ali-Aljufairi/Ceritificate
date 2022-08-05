from Generate_Certificate import Generate_Certificate
from Convertpdf import Convert_pdf

if __name__ == "__main__":
    with open("Names.txt") as file:
        NAMES = file.readlines()
        NAMES = [name.strip() for name in NAMES]
        NAMES.pop(-1)
        NAMES.sort()

    text_y_position = int(input("Enter the text y position: "))
    font_size = int(input("Enter the font size: "))
    COLOR = input("Enter the color: ").lstrip("#")

    FONT = "Font/Arvo-Regular.ttf"
    CERTIFICATE = "Sample Certificate/Ceritifcate.png"
    rcolor = tuple(int(COLOR[i:i + 2], 16) for i in (0, 2, 4))

    Generate_Certificate(NAMES, CERTIFICATE, FONT, rcolor, text_y_position, font_size)
    Convert_pdf(NAMES)

#
#
