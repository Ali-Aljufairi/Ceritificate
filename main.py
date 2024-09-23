import argparse
from modules.certifcate import generate_certificate
from modules.convert_pdf import convert_pdf
import modules.data_clean as data_clean
from modules.file_manger import ensure_directories_exist, download_default_font, create_default_white_certificate, list_files_in_directory
from modules.user_input import select_file_from_list, get_color_input
from modules.zip_manager import zip_pdfs, clean_up_pdfs


def cli_main():
    """Main function for CLI interactions and certificate generation."""
    ensure_directories_exist(["cert", "font", "PDFs", "Genrated Certificates", "csv", "zip"])

    # If no font files are present, download a default font
    if not list_files_in_directory("font", ".ttf"):
        download_default_font()

    # If no certificate templates are found, generate a default white certificate
    if not list_files_in_directory("cert", ".png"):
        create_default_white_certificate()

    # CLI argument parser
    parser = argparse.ArgumentParser(description="Generate certificates, convert them to PDFs, and zip them.")
    
    # Add arguments for optional file selections
    parser.add_argument("csv_file", nargs='?', help="CSV file containing names", default=None)
    parser.add_argument("certificate", nargs='?', help="Certificate template file", default=None)
    parser.add_argument("font", nargs='?', help="Font file for name text", default=None)
    parser.add_argument("--color", help="Hex color for name text", default="343434")
    parser.add_argument("--font_size", type=int, help="Font size for the name", default=85)
    parser.add_argument("--name_position", type=int, help="Vertical position for the name", default=640)
    
    args = parser.parse_args()

    # Choose CSV file (names) interactively if not provided
    if not args.csv_file:
        args.csv_file = select_file_from_list("csv", ".csv", message="Choose a CSV file with names")

    # Choose certificate template interactively if not provided
    if not args.certificate:
        args.certificate = select_file_from_list("cert", ".png", message="Choose a certificate template")

    # Choose font interactively if not provided
    if not args.font:
        args.font = select_file_from_list("font", ".ttf", message="Choose a font for the name text")

    try:
        # Organize data from CSV
        names = data_clean.organize_data(args.csv_file)
    except Exception as e:
        print(f"Error processing CSV file {args.csv_file}: {e}")
        exit(1)

    # Get color input
    rcolor = get_color_input(args.color)

    # Generate certificate and convert to PDF
    try:
        generate_certificate(
            names,
            f"cert/{args.certificate}",
            f"font/{args.font}",
            rcolor,
            args.name_position,
            args.font_size,
            args.font,
            50, 820
        )
    except Exception as e:
        print(f"Error generating certificates: {e}")
        exit(1)

    try:
        convert_pdf(names)
    except Exception as e:
        print(f"Error converting images to PDFs: {e}")
        exit(1)

    # Prompt for the zip filename
    zip_name = input("Enter the name for the zip file (without extension): ").strip()
    if not zip_name:
        print("No zip name provided, exiting.")
        exit(1)

    # Zip the PDFs and clean up
    zip_pdfs(zip_name)
    clean_up_pdfs()

    # Ask if user wants to regenerate certificates
    while input("Do you want to regenerate certificates and PDFs? (y/n): ").lower() == 'y':
        cli_main()


if __name__ == "__main__":
    cli_main()