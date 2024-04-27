from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np

root=Tk()
root.geometry('1000x800')
root.title("Numerical Analysis Calculator")
root.config(bg='white')
root.resizable(0,0)
import subprocess
import os

def run_file(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    subprocess.run(["python", file_path])





