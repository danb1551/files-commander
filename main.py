import tkinter as tk
from tkinter import ttk
import os


root = tk.Tk()
WIDTH = 960
HEIGHT = 580
root.geometry(f"{WIDTH}x{HEIGHT}")

rp = tk.Frame(bg="red", height=HEIGHT*0.3, width=WIDTH) # Remote panel for controls
#dp = tk.Frame() # Directory panel for list of most used directory (I will add it later)

dir_entry = ttk.Entry(rp, width=WIDTH)
def get_current_dir():
    return os.getcwd()

def change_directory(dir):
    os.system(f"cd {dir}")
    dir_entry.insert(get_current_dir)

rp.pack(fill="x")

root.mainloop()