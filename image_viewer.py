import tkinter as tk
import os
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Image Viewer')
root.iconbitmap('Images/icon.ico')

# Loading in images from 'Images' folder
image_list = []
for location in os.listdir('Images'):
    if '.png' not in location and '.jpeg' not in location:
        continue
    image = ImageTk.PhotoImage(Image.open('Images/'+location).resize((640,480)))
    image_list.append(image)

page_number = 0

# Function to refresh widgets when page is changed
def change_page(delta):
    global page_number
    page_number += delta
    current_image(page_number).grid(row=0, column=0, columnspan=3)
    back_button(page_number).grid(row=1, column=0)
    exit_button().grid(row=1, column=1)
    next_button(page_number).grid(row=1, column=2)
    status_bar(page_number).grid(row=2, column=0, columnspan=3, sticky=tk.E)

## Functions to define new widgets

def current_image(page_number):
    image_label = tk.Label(root, image=image_list[page_number])
    return image_label

def back_button(page_number):
    button = tk.Button(root, text='<<', command=lambda: change_page(-1), state=tk.DISABLED if page_number==0 else tk.NORMAL)
    return button

def exit_button():
    button = tk.Button(root, text='Exit', command=root.destroy)
    return button

def next_button(page_number):
    button = tk.Button(root, text='>>', command=lambda: change_page(1), state=tk.DISABLED if page_number==len(image_list)-1 else tk.NORMAL)
    return button

def status_bar(page_number):
    status_bar_label = tk.Label(root, text=f'Image {page_number+1} of {len(image_list)}')
    return status_bar_label

change_page(0)

root.mainloop()