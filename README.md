# TSV to CSV Converter

## Overview
This Python script converts TSV (Tab-Separated Values) files to CSV (Comma-Separated Values) format. It allows you to select a TSV file and automatically saves the converted CSV file in the same directory.

## Requirements
- Python 3.x
- `tkinter` (included with Python standard library)
- `csv` (included with Python standard library)
- PyInstaller (for creating an executable)

## How to Use

### Running the Script
1. **Download the script**: Obtain the `tsv_to_csv.py` file.
2. **Run the script**:
   - If you have Python installed, you can run the script from the command line:
     ```bash
     python tsv_to_csv.py
     ```
   - If you have the executable (e.g., `tsv_to_csv.exe`), simply double-click it to run.

3. **Select a TSV file**: A file dialog will open, prompting you to select the TSV file you want to convert.

4. **Conversion**: The script will convert the selected TSV file and save the CSV file in the same directory with the same name.

### Creating an Executable
To create a standalone executable that can run on any machine:
1. Install PyInstaller if you haven't:
   ```bash
   pip install pyinstaller
2. Package the script:
```bash
pyinstaller --onefile --noconsole tsv_to_csv.py
```
3. Locate the executable in the `dist` folder. You can distribute this file without needing Python installed on the target machine.

## Notes

-   The executable will not open a console window when run.
-   Make sure to test the script/executable in your environment.