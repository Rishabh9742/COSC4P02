import tkinter as tk
import urllib.request
import csv
from PIL import Image, ImageTk

def show_data(line_num):
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        try:
            title, description, image_url = data[line_num]
        except IndexError:
            tkinter.messagebox.showerror("Error", "Line number not found in the CSV")
            return
        
        label_title.config(text=title)
        label_description.config(text=description)
        
        image = Image.open(urllib.request.urlopen(image_url))
        image.thumbnail((500, 500), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label_image.config(image=photo)
        label_image.image = photo

root = tk.Tk()
root.title("Data Display")
root.geometry("500x500")

line_num = 0

label_title = tk.Label(root, font=("TkDefaultFont", 16))
label_title.pack()

label_description = tk.Label(root, font=("TkDefaultFont", 14))
label_description.pack()

label_image = tk.Label(root)
label_image.pack()

def prev_data():
    global line_num
    if line_num > 0:
        line_num -= 1
        show_data(line_num)
    else:
        tkinter.messagebox.showerror("Error", "Already at the first line")

button_prev = tk.Button(root, text="Previous", command=prev_data)
button_prev.pack(side="left")

def next_data():
    global line_num
    line_num += 1
    show_data(line_num)

button_next = tk.Button(root, text="Next", command=next_data)
button_next.pack(side="right")

show_data(line_num)

root.mainloop()
