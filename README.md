# Automating the processing of Excel files

## Description
This project is designed to automate routine data processing tasks in Excel files using Python. It allows you to combine data from multiple sheets, sort them, and save them to a new Excel file.

## Project structure
- `data/` - directory with sample source data.
- `scripts/` - directory with scripts:
  - `combine_sheets.py` - script for data merging.
  - `sort_data.py` - script for sorting data.
  - `save_to_excel.py` - script for saving data in Excel.
  - `main.py` - the main script to perform all actions.
- `requirements.txt` - file with dependencies.
- `.gitignore` - file to exclude unnecessary files from commits.
- `README.md` - file with project description.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/username/my_python_project.git
    cd my_python_project
    ```
2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Run the main script to process the data:
```bash
python scripts/main.py
