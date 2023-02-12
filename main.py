import tkinter as tk
import csv
from PIL import Image, ImageTk
import urllib.request

line_num = 0

def show_data(line_num):
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        global data
        data = list(reader)
        
        try:
            title, description, image_url = data[line_num]
        except IndexError:
            tk.messagebox.showerror("Error", "Line number not found in the CSV")
            return
        
        label_title.config(text=title)
        label_description.config(text=description)
        
        image = Image.open(urllib.request.urlopen(image_url))
        image = image.resize((250, 250), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        label_image.config(image=image)
        label_image.image = image
        
        line_text = f"Line {line_num + 1} of {len(data)}"
        label_line.config(text=line_text)

def next_line():
    global line_num
    if line_num < len(data) - 1:
        line_num += 1
        show_data(line_num)

def previous_line():
    global line_num
    if line_num > 0:
        line_num -= 1
        show_data(line_num)

root = tk.Tk()
root.title("CSV Data Display")

label_title = tk.Label(root, text="")
label_title.pack()

label_description = tk.Label(root, text="")
label_description.pack()

label_image = tk.Label(root, image=None)
label_image.pack()

button_next = tk.Button(root, text="Next", command=next_line)
button_next.pack()

button_previous = tk.Button(root, text="Previous", command=previous_line)
button_previous.pack()

label_line = tk.Label(root, text="")
label_line.pack()

show_data(line_num)
root.mainloop()
