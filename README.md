# Excel Files Processing Automation Project

## Description
This project is designed to automate routine tasks of processing data in Excel files using Python. It allows you to merge data from multiple sheets, sort it, and save it to a new Excel file.

## Project Structure
- `data/` - Directory containing sample input data.
- `scripts/` - Directory containing scripts:
  - `combine_sheets.py` - Script for merging data.
  - `sort_data.py` - Script for sorting data.
  - `save_to_excel.py` - Script for saving data to an Excel file.
  - `main.py` - Main script that orchestrates all actions.
- `requirements.txt` - File containing dependencies.
- `.gitignore` - File to exclude unnecessary files from commits.
- `README.md` - Project description file.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/username/my_python_project.git
    cd my_python_project
    ```
2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Run the main script to process the data:
```bash
python scripts/main.py
```

## License
This project is licensed under the MIT License. For more information, see the LICENSE file.

## Initializing Git and Uploading to GitHub

### 1. Initialize the Git repository
In the root folder of your project, run the following commands:
```bash
git init
git add .
git commit -m "Initial commit"
```

### 2. Create a GitHub repository
Go to GitHub and create a new repository.
Follow the instructions on the screen to link your local repository to the remote:
```bash
git remote add origin https://github.com/username/my_python_project.git
git branch -M main
git push -u origin main
```

### 3. Adding a license file
Don't forget to add a license file if you want to make the project open-source:
```bash
touch LICENSE
```
Then, add the license text, such as the MIT License, and commit the changes:
```bash
git add LICENSE
git commit -m "Add LICENSE file"
git push
