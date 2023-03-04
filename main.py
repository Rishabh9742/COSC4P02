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
        
def jump_to_line():
            global line_num
            line_num = int(nodeText.get()) -1
            show_data(line_num)           

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
