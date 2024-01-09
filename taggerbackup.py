##Import packages
from tkinter import *
from PIL import ImageTk, Image
from os import listdir
from os.path import isfile, join

##Initalize window (ws = windowsize)
ws = Tk()
ws.title('floatme')
#Window dimensions
#Background color
ws.config(bg='#443644')
def savetext():
    itm = lb.get(lb.curselection())
    im = Image.open("/home/matt/taggerpy/image/100_Skinhead/"+str(itm))
    imtxt = "/home/matt/taggerpy/image/100_Skinhead/"+str(itm)[:-4] +str(".txt")
    f = open(imtxt,'r')
    file_contents = f.read()

    print("savetext")
    inp = text.get(1.0, "end")
    f = open(imtxt, "w")
    f.write(inp)
    f.close()


##Switch image function, needs refactoring
def showSelected(event):
    print("CRAY")
    itm = lb.get(lb.curselection())
    #var.set(itm)
    im = Image.open("/home/matt/taggerpy/image/100_Skinhead/"+str(itm))
    imtxt = "/home/matt/taggerpy/image/100_Skinhead/"+str(itm)[:-4] +str(".txt")
    f = open(imtxt,'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
    print(imtxt)
    size = (200,200)
    im = im.resize(size)
    im = ImageTk.PhotoImage(im)
    print("show")
    #im.show()
    label.configure(image = im)
    label.image = im    
    var.set(file_contents)
    text.delete("1.0","end")
    text.insert('1.0',file_contents)

def appendall():
    print("running!")
    x = 0
    for f in listdir("image/100_Skinhead"):
        x + 1
        if isfile(join("image/100_Skinhead", f)) and ".txt" in f:
            print(f)
            inp = textSearch.get(1.0, "end")
            f = open(join("image/100_Skinhead", f),'a')
            f.write(","+ inp.rstrip())
            f.close()


##Block for displaying an image file
##Opens an image first so not to throw erros, needs fixing with trycatch.
im = Image.open("/home/matt/taggerpy/image/100_Skinhead/a7db2a4b629a53647b38be377e2e121f_noface.jpg")
##Resize test code, needs refactoring
size = (200,200)
im = im.resize(size)
im = ImageTk.PhotoImage(im)

left_frame = Frame(ws, width=200, height=200)
left_frame.grid(row=0, column=0)
left_frame.config(bg="orange")

right_frame = Frame(ws, width=200, height=200)
right_frame.grid(row=0, column=1)
right_frame.config(bg="")


label = Label(right_frame, image = im)
label.grid(row=0, column=0)
##Listbox and label for displaying prompt info
var =StringVar()
lb = Listbox(left_frame, width=30, height=20)
lb.grid(row=0, column=0)
textSearch = Text(left_frame, height=8)
textSearch.config(width=5)
textSearch.grid(row=1, column=0)
appendbutton = Button(left_frame,text="append", command=appendall)
appendbutton.grid(row=3,column=0)
#lb.place(relx = 0.5,rely = 0.5,anchor = 'center')

##Loop through directory and get all instances of .jpg files
x = 0
for f in listdir("image/100_Skinhead"):
    x + 1
    if isfile(join("image/100_Skinhead", f)) and ".jpg" in f:
        lb.insert(x, str(f))

##text
#disp = Label(ws, textvariable=var)
#disp.config(height=5, width=30)
#disp.grid(row=2,column=1)
#disp.place(relx = 0.5,rely = 0.5,anchor = 'se')

##Run showselected function when a selection is made on the listbox.
lb.bind("<<ListboxSelect>>",showSelected)
text = Text(right_frame, height=8)
text.grid(row=1, column=0)

savebutton = Button(right_frame,text="hero", command=savetext)
savebutton.grid(row=3,column=0)
##Mainloop run
ws.mainloop()

