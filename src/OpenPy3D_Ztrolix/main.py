import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from tqdm import tqdm
from PIL import Image, ImageTk
import os
import sys
import random
import math
import time
import requests
import urllib.request
from zipfile import ZipFile
from pathlib import Path
from tkinter import filedialog
import logging
from tqdm import tqdm_notebook as tqdmnote


os.system("scripts\\updater.bat")

# Function to display a message box
def cube():
    messagebox.showinfo("OpenPy3D - Cube", "Generatin0g cube...")
    os.system("scripts\\cube.py")

def cubeplus():
    messagebox.showinfo("OpenPy3D - Cube+", "Generating cube+...")
    os.system("scripts\\cubeplus.py")

def sphere():
    messagebox.showinfo("OpenPy3D - Sphere", "Generating sphere...")
    os.system("scripts\\sphere.py")

def piramid():
    messagebox.showinfo("OpenPy3D - Piramid", "Generating piramid...")
    os.system("scripts\\piramid.py")

def pip():
    messagebox.showinfo("OpenPy3D - Pip", "Updating pip...")
    os.system("scripts\\updater.bat")

def python():
    messagebox.showinfo("OpenPy3D - Python", "Updating python...")
    os.system("scripts\\pythonup.py")

def close():
    os.system("scripts\\close.vbs")
    root.quit()
    quit()
    exit()
    sys.exit()

def console():
    messagebox.showinfo("OpenPy3D - Console", "Loading Console()...")
    os.system("scripts\\console.py")
def custom():
    messagebox.showinfo("OpenPy3D - Console", "Loading Console()...")
    os.system("scripts\\console.py")

def new():
    os.system("scripts\\new.py")
def open():
    messagebox.showinfo("OpenPy3D - Open Projects", "Loading Projects...")
    os.system("scripts\\open.py")

# Create the main window
root = tk.Tk()
root.title("OpenPy3D - Menu")
root.iconbitmap("icon_4.ico")
root.resizable(False, False)
root.maxsize(300, 250)
root.minsize(300, 250)
root.geometry("300x250")  # Set the window size

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Options", menu=file_menu)
file_menu.add_command(label="New Project", command=new)
file_menu.add_command(label="Open Project", command=open)
file_menu.add_separator()
file_menu.add_command(label="Generate Cube", command=cube)
file_menu.add_command(label="Generate Cube+", command=cubeplus)
file_menu.add_command(label="Generate Sphere", command=sphere)
file_menu.add_command(label="Generate Piramid", command=piramid)
file_menu.add_separator()
file_menu.add_command(label="Update Pip", command=pip)
file_menu.add_command(label="Update Python", command=python)
file_menu.add_separator()
file_menu.add_command(label="Restart OpenPy3D", command=close)
file_menu.add_command(label="Exit OpenPy3D", command=close)

cube_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Commands", menu=cube_menu)
cube_menu.add_command(label="Console()", command=console)

# Create buttons in the center of the window
button_frame = tk.Frame(root)
button_frame.pack(expand=True)

Label(button_frame, text = 'OpenPy3D', font =('Verdana', 15)).pack(side = TOP, pady = 10)


button1 = tk.Button(button_frame, text="Open Projects", width="30",height="3", command=open)
button2 = tk.Button(button_frame, text="New Project", width="30",height="3", command=new)
button1.pack(pady=10)
button2.pack(pady=10)

# Run the main loop
root.mainloop()