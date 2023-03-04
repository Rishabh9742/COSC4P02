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
        
def delete_from_csv():
    try:
        index = int(rowDel.get()) - 1
        with open(root.filename, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        with open(root.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows[:index] + rows[index+1:])
            tk.messagebox.showinfo("Success", "Row deleted from CSV file.")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error occurred: {str(e)}")        

def clear_text():
    title_entry.delete(0,tk.END)
    description_entry.delete(0,tk.END)
    image_url_entry.delete(0,END)

def main():
    root = tk.Tk()
    root.title("CSV Data Display")

    label_title = tk.Label(root, text="")
    label_title.grid(row=0, column=0, columnspan=3)

    label_description = tk.Label(root, text="")
    label_description.grid(row=1, column=0, columnspan=3)

    label_line = tk.Label(root, text="")
    label_line.grid(row=2, column=0, columnspan=3)

    label_image = tk.Label(root, image=None)
    label_image.grid(row=3, column=0, columnspan=3)

    button_previous = tk.Button(root, text="<", command=previous_line)
    button_previous.grid(row=4, column=0, sticky='E')

    nodeText = tk.Entry(root, width=3)
    nodeText.grid(row=4, column=1)

    button_next = tk.Button(root, text=">", command=next_line)
    button_next.grid(row=4, column=2, sticky='W')

    button_go_to_line = tk.Button(root, text="Jump to node", command=jump_to_line)
    button_go_to_line.grid(row=6, column=1)

    show_data(line_num)
    root.mainloop()

if __name__ == '__main__':
    main()
