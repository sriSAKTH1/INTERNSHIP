import tkinter as tk
from tkinter import filedialog

def open_file():
   
    root = tk.Tk()
    root.withdraw()  

    file_path = filedialog.askopenfilename()
    if file_path:  
        scan_file(file_path)

def scan_file(file_path):
    
    try:
        with open(file_path, "rb") as f:
            file_content = f.read()

        virus_signature = rb"X50!P%@AP[4\PZX%$(P^)&CC)7}$ESPRIT_STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
        if virus_signature in file_content:
            print("Virus found in file:", file_path)
        else:
            print("Virus not found in file:", file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
open_file()
