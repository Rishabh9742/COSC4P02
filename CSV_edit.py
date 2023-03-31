from tkinter import *
from tkinter import ttk 
import tkinter as tk
import tkinter.messagebox
import csv
from PIL import Image, ImageTk
import urllib.request
from tkinter import filedialog
import json

def select_json_file():
    root.filename = filedialog.askopenfilename(initialdir="./", title="Select JSON file", filetypes=(("JSON files", "*.json"), ("all files", "*.*")))
    csv_file_path.config(text=root.filename)
    
def append_to_json():
    try:
        with open(root.filename, 'r+') as file:
            data = json.load(file)
            if not data:
                data = []
            data.append({"title": title_entry.get(), "description": description_entry.get(), "image_url": image_url_entry.get()})
            file.seek(0)
            json.dump(data, file)
            file.truncate()
            tk.messagebox.showinfo("Success", "Data appended to the JSON file.")
            clear_text()
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error occurred: {str(e)}")
        clear_text()
        
def delete_from_json():
    try:
        index = int(rowDel.get()) - 1
        with open(root.filename, 'r+') as file:
            data = json.load(file)
            del data[index]
            file.seek(0)
            json.dump(data, file)
            file.truncate()
            tk.messagebox.showinfo("Success", "Row deleted from JSON file.")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error occurred: {str(e)}")        

def clear_text():
    title_entry.delete(0,tk.END)
    description_entry.delete(0,tk.END)
    image_url_entry.delete(0,END)

root = tk.Tk()
root.geometry("200x375")
root.title("CSV Data Appender")

csv_file_label = tk.Label(root, text="Select a CSV file:")
csv_file_label.pack()

csv_file_path = tk.Label(root, text="No CSV file selected")
csv_file_path.pack()

csv_file_button = tk.Button(root, text="Browse", command=select_json_file, relief=RAISED)
csv_file_button.pack(pady=10)

title_label = tk.Label(root, text="Title:")
title_label.pack()

title_entry = tk.Entry(root)
title_entry.pack()

description_label = tk.Label(root, text="Description:")
description_label.pack()

description_entry = tk.Entry(root)
description_entry.pack()

image_url_label = tk.Label(root, text="Image URL:")
image_url_label.pack()

image_url_entry = tk.Entry(root)
image_url_entry.pack()

delete_button = tk.Button(root, text="Clear Text", command=clear_text, relief=RAISED)
delete_button.pack(pady=10)

append_button = tk.Button(root, text="Append to CSV", command=append_to_json, relief=RAISED)
append_button.pack(pady=10)

deleteRow_button = tk.Button(root, text="Delete from CSV", command=delete_from_json, relief=RAISED)
deleteRow_button.pack(pady=10)

rowDel = tk.Entry(root, width=3)
rowDel.pack()

root.mainloop()
