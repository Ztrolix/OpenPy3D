import os
import requests
import urllib.request
from zipfile import ZipFile
from pathlib import Path
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog
import logging
import sys
import time

def download_files():
    print("Downloading Python...")

    installer_url = 'https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe'

    try:
        with requests.get(installer_url, stream=True) as response:
            with open("python-3.11.4-amd64.exe", 'wb') as f:
                total_size = int(response.headers.get('content-length', 0))
                with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        pbar.update(len(chunk))
        print("Download complete!")
    except Exception as e:
        print("An error occurred while downloading the installer:", e)

def install_files():
    print("Installing Python...")
    os.system("python-3.11.4-amd64.exe")
    print("Installation complete!")
    
def main():
    download_files()
    install_files()
    print("Process completed successfully!")
    
if __name__ == "__main__":
    main()