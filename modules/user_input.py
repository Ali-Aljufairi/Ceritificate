import os
import inquirer
from inquirer.errors import ValidationError


def list_files_in_directory(directory, extension=None):
    """List files in the specified directory, filter by extension if provided."""
    path = os.path.abspath(directory)
    if extension:
        files = [file for file in os.listdir(path) if file.endswith(extension)]
    else:
        files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

    return files


def select_file_from_list(directory, extension=None, message="Choose a file"):
    """Prompt user to select a file from the list using arrow keys."""
    try:
        files = list_files_in_directory(directory, extension)
        if not files:
            raise FileNotFoundError(f"No {extension or ''} files found in {directory}.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)

    questions = [
        inquirer.List('selected_file', message=message, choices=files)
    ]
    answer = inquirer.prompt(questions)
    if not answer:
        print("No file selected. Exiting.")
        exit(1)
    return answer['selected_file']


def validate_color_hex(color):
    """Validate that the color is a proper 6-character hex string."""
    if len(color) != 6 or not all(c in '0123456789abcdefABCDEF' for c in color):
        raise ValidationError(f"{color} is not a valid hex color.")
    return True


def get_color_input(default_color="343434"):
    """Prompt user for hex color input with a default."""
    while True:
        try:
            color_input = input(f"Enter the color in hex format (default: {default_color}): ").strip() or default_color
            validate_color_hex(color_input)
            return tuple(int(color_input[i:i + 2], 16) for i in (0, 2, 4))
        except ValidationError as e:
            print(e)