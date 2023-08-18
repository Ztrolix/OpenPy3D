import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
import sys

# Function to display a message box
def cube():
    messagebox.showinfo("OpenPy3D - Cube", "Generating cube...")
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

def custom():
    messagebox.showinfo("OpenPy3D - Custom", "Loading Custom()...")
    messagebox.showinfo("OpenPy3D - Custom", "ERROR: Loading Custom()!")

def submit():
 
    name=name_var.get()
     
    print("Console: " + name)
    if name == "Custom()":
        custom()
    elif name == "Cube()":
        cube()
    elif name == "Piramid()":
        piramid()
    elif name == "Sphere()":
        sphere()
    elif name == "Console()":
        console()
    else:
        print("ERROR: '" + name + "' is not a function.")
     
    name_var.set("")

# Create the main window
root = tk.Tk()
root.title("OpenPy3D - ConsoleEditor")
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

Label(button_frame, text = 'OpenPy3D - ConsoleEditor', font =('Verdana', 15)).pack(side = TOP, pady = 10)


sub_btn=tk.Button(button_frame,text = 'Enter', command = submit)
name_var=tk.StringVar()
name_entry = tk.Entry(button_frame,textvariable = name_var, font=('calibre',20,'normal'))
sub_btn.pack(pady=10)
name_entry.pack(pady=10)

# Run the main loop
root.mainloop()