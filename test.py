from tkinter import *
from PIL import ImageTk, Image

from os import listdir
from os.path import isfile, join
root = Tk()
root.title("floatme")
root.config(bg='#443644')

left_frame = Frame(root, width=200, height=200)
left_frame.grid(row=0,column=0, padx=10, pady=5)
left_frame.config(bg="orange")

right_frame = Frame(root, width=200, height=200)
right_frame.grid(row=0, column=1, padx=10, pady=10)
right_frame.config(bg="red")
Label(left_frame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)
root.mainloop()