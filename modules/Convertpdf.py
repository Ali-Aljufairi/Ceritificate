import img2pdf

def Convert_pdf(names: list):
    #hello
    names = [name[0] for name in names]
    for name in names:
        with open("PDFs/{}.pdf".format(name), "wb") as f:
            f.write(img2pdf.convert(["Genrated Certificates/{}.png".format(name)]))