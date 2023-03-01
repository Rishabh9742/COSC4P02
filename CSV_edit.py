from tkinter import *
from tkinter import ttk
import tkinter as tk
import csv
from PIL import Image, ImageTk
import urllib.request
from tkinter import filedialog

def select_csv_file():
    root.filename = filedialog.askopenfilename(initialdir="./", title="Select CSV file", filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    csv_file_path.config(text=root.filename)

def append_to_csv():
    try:
        with open(root.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title_entry.get(), description_entry.get(), image_url_entry.get()])
            tk.messagebox.showinfo("Success", "Data appended to the CSV file.")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error occurred: {str(e)}")

def clear_text():
    title_entry.delete(0,tk.END)
    description_entry.delete(0,tk.END)
    image_url_entry.delete(0,END)

root = tk.Tk()
root.geometry("200x350")
root.title("CSV Data Appender")

csv_file_label = tk.Label(root, text="Select a CSV file:")
csv_file_label.pack()

csv_file_path = tk.Label(root, text="No CSV file selected")
csv_file_path.pack()

csv_file_button = tk.Button(root, text="Browse", command=select_csv_file, relief=RAISED)
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

read_button = tk.Button(root, text="Read from CSV", command=append_to_csv, relief=RAISED)
read_button.pack(pady=10)

append_button = tk.Button(root, text="Append to CSV", command=append_to_csv, relief=RAISED)
append_button.pack(pady=10)

delete_button = tk.Button(root, text="Clear Text", command=clear_text, relief=RAISED)
delete_button.pack(pady=10)

root.mainloop()
