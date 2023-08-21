import os
import requests
import urllib.request
from zipfile import ZipFile
from pathlib import Path
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import logging
import sys
import time
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
import sys

def submit():
 
    projectName=name_var.get()
     
    print("ProjectName: " + projectName)
     
    name_var.set("")
    f = open("projects\\temp.txt", "w")
    f.write(str(projectName))
    f.close()
    main()

def download_files():
    f = open("projects\\temp.txt", "r")
    projectName = f.read()
    print("Downloading Project Files...")

    installer_url = 'https://github.com/Ztrolix/OpenPy3D/raw/main/Template.zip'

    try:
        with requests.get(installer_url, stream=True) as response:
            with open(str(projectName) + ".zip", 'wb') as f:
                total_size = int(response.headers.get('content-length', 0))
                with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        pbar.update(len(chunk))
        print("Download complete!")
    except Exception as e:
        print("An error occurred while downloading the files:", e)

def extract_project():
    f = open("projects\\temp.txt", "r")
    projectName = f.read()
    try:
        print(f"Extracting Project Files...")
        with ZipFile(projectName + ".zip", 'r') as zObject:
            destination = Path("projects/" + projectName + "/")
            destination.mkdir(parents=True, exist_ok=True)
            file_count = len(zObject.infolist())
            with tqdm(total=file_count) as pbar:
                for file_info in zObject.infolist():
                    zObject.extract(file_info, path=destination)
                    pbar.update(1)
    except Exception as e:
        print("An error occurred while extracting the modpack:", e)
    
def main():
    root.withdraw()
    download_files()
    extract_project()
    print("Process completed successfully!")
    
def nameProject():
    root = tk.Tk()
    root.title("OpenPy3D - Project Creator")
    root.iconbitmap("icon_4.ico")
    root.resizable(False, False)
    root.maxsize(350, 150)
    root.minsize(350, 150)
    root.geometry("350x150")  # Set the window size

    # Create buttons in the center of the window
    button_frame = tk.Frame(root)
    button_frame.pack(expand=True)

    img = ImageTk.PhotoImage(Image.open("icon_4.png"))
    panel = Label(root, image = img)

    Label(button_frame, text = 'Project Name', font =('Verdana', 15)).pack(side = TOP, pady = 10)

    sub_btn=tk.Button(button_frame,text = 'Enter', command = submit)
    name_var=tk.StringVar()
    name_entry = tk.Entry(button_frame,textvariable = name_var, font=('calibre',20,'normal'))
    sub_btn.pack(pady=10)
    name_entry.pack(pady=10)

    # Run the main loop
    root.mainloop()

nameProject()