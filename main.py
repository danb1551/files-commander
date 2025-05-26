import tkinter as tk
from tkinter import ttk
import os


root = tk.Tk()
WIDTH = 960
HEIGHT = 580
root.geometry(f"{WIDTH}x{HEIGHT}")

rp = tk.Frame(bg="gray", height=HEIGHT*0.2, width=WIDTH) # Remote panel for controls
#dp = tk.Frame() # Directory panel for list of most used directory (I will add it later)

dir_list = tk.Frame(root, width=WIDTH, height=HEIGHT*0.8)

dir_entry = ttk.Entry(rp, width=WIDTH)
def get_current_dir():
    return os.getcwd()

def set_search():
    rp = tk.Frame(bg="gray", height=HEIGHT*0.2, width=WIDTH)
    dir_entry = ttk.Entry(rp, width=WIDTH)
    dir_entry.delete(0, tk.END)
    dir_entry.insert(0, string=str(get_current_dir()))
    dir_entry.grid(pady=25, padx=25, column=1, row=1)
    rp.pack(fill="x")

def change_directory(*args):
    try:
        dir = dir_entry.get()
        os.system(f"cd {dir}")
        dir_entry.delete(0, tk.END)
        dir_entry.insert(0, string=dir)
        for child in dir_list.winfo_children():
            child.destroy()
        #set_search()
        for items in os.listdir(dir):
            tk.Label(dir_list, text=items).pack()
    except WindowsError as e:
        #dir_entry.delete(0, tk.END)
        #dir_entry.insert(0, string=get_current_dir)
        print("zas ta chyba", e)

dir_entry.delete(0, tk.END)
dir_entry.insert(0, string=str(get_current_dir()))
dir_entry.grid(pady=25, padx=25, column=1, row=1)
rp.pack(fill="x")
dir_list.pack()
root.bind("<Return>", change_directory)

root.mainloop()