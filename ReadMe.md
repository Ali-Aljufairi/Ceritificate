
# Certificate Generator

This is a Python project that generates certificates for a list of names provided in a CSV file. The certificates are generated in PNG format and can be converted to PDF using the included `Convert_pdf` function. All generated PDFs can be zipped for easy distribution, and the project can be managed using the `uv` package manager for faster and more efficient operations.

## Why Use `uv`?

This project now supports `uv`, an extremely fast Python package and project manager written in Rust. `uv` is a comprehensive tool that can replace traditional tools like `pip`, `virtualenv`, and `poetry`, while offering blazing-fast performance and efficient project management. If you're new to `uv`, this README will guide you through the process of using it with this project.

`uv` highlights include:
- **Fast**: 10-100x faster than `pip`.
- **Python Version Management**: Manage and switch between Python versions seamlessly.
- **Comprehensive**: Single tool that replaces `pip`, `poetry`, `pyenv`, and more.


##
```bash
├── cert
├── compose.yml
├── csv
├── Dockerfile
├── font
├── 'Genrated Certificates'
├── main.py
├── modules
│  ├── __pycache__
│  ├── certifcate.py
│  ├── convert_pdf.py
│  ├── data_clean.py
│  ├── file_manger.py
│  ├── sendmail.py
│  ├── user_input.py
│  └── zip_manager.py
├── PDFs
├── pyproject.toml
├── ReadMe.md
├── run.sh
├── uv.lock
└── zip
```



## Installation

1. Clone the repository to your local machine:

    ```bash
     https://github.com/Ali-Aljufairi/Ceritificate 
     cd Certificate 
    ```

2. Install `uv`:
   - On macOS and Linux:

     ```bash
     curl -LsSf https://astral.sh/uv/install.sh | sh
     ```

   - On Windows:

     ```bash
     powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
     ```

   - Alternatively, install it with `pip`:

     ```bash
     pip install uv
     ```

3. Install dependencies using `uv`:

    ```bash
    uv pip sync
    ```

   This installs all the required dependencies, based on the `pyproject.toml` or `requirements.txt` file.

4. Initialize a virtual environment:

    ```bash
    uv venv
    ```

   This creates a virtual environment in the project directory.

5. Activate the environment:

   - On macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

## Usage

1. Place a CSV file with the list of names in the `csv/` directory. If no CSV file exists, a default one will be created.

2. Run the project:

    ```bash
    uv run python main.py
    ```

3. You will be prompted to select:
   - A CSV file containing names.
   - A certificate template from the `cert/` directory.
   - A font for the text from the `font/` directory.

4. Enter the desired color for the certificate text when prompted.

5. The certificates will be generated in the `Generated Certificates` directory, converted to PDFs in the `PDFs` directory, and zipped into a single file in the `zip` directory.
