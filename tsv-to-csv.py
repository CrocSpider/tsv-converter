import csv
import os
import tkinter as tk
from tkinter import filedialog

# Set up a basic Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Prompt the user to select a TSV file
tsv_file_path = filedialog.askopenfilename(title="Select a TSV file", filetypes=[("TSV files", "*.tsv")])

if tsv_file_path:  # Proceed if a file was selected
    # Define the CSV file path in the same directory
    csv_file_path = os.path.splitext(tsv_file_path)[0] + '.csv'
    
    with open(tsv_file_path, 'r') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in reader:
                writer.writerow(row)

    print(f"Converted {tsv_file_path} to {csv_file_path}")
else:
    print("No input file selected.")
    