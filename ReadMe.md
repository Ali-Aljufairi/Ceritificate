
# Certificate Generator

This is a Python project that generates certificates for a list of names provided in a CSV file. The certificates are generated in PNG format and can be converted to PDF using the included `Convert_pdf` function.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using pip: `pip install -r requirements.txt`

## Usage

1. Place a CSV file with the list of names in the root directory of the project.
2. Run the `main.py` file.
3. Enter the desired color for the certificate when prompted.
4. The certificates will be generated in the `cert` directory and a PDF file will be generated in the root directory.

## Customization

The project can be customized by modifying the following variables in the `main.py` file:

- `Project_Postion`: The y-position of the project name on the certificate.
- `font_size_project`: The font size of the project name on the certificate.
- `Name_Postion`: The y-position of the name on the certificate.
- `font_size_name`: The font size of the name on the certificate.
- `Project_FONT`: The font file for the project name.
- `Name_Font`: The font file for the name.
- `CERTIFICATE`: The template certificate file.
- `rcolor`: The color of the certificate in RGB format.

## Example

Here's an example of how to use the project:

1. Create a CSV file with the list of names.
2. Clone the repository to your local machine.
3. Install the required dependencies using pip: `pip install -r requirements.txt`
4. Place the CSV file in the root directory of the project.
5. Run the `main.py` file.
6. Enter the desired color for the certificate when prompted.
7. The certificates will be generated in the `cert` directory and a PDF file will be generated in the root directory.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

Let me know if you need any further assistance!