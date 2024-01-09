##Import packages
from tkinter import *
from PIL import ImageTk, Image
from os import listdir
from os.path import isfile, join

##Loop through given directory, could return an array?
path = "/home/matt/taggerpy/image/100_Skinhead/"
#If we're going to refresh the file list, the array must be cleared before doing so
files = []
def getfiles():
    x = 0
    for f in listdir(path):
        ##Issue with using x as index to add should be direct iteration
        if isfile(join(path, f)) and ".jpg" in f:
            x += 1
            print(x)
            #save to list, might be useful
            files.append(str(f))
            #insert directly from loop, easier that doing it from the list right now.
            lb.insert(x, str(f))

def getPath():
    impath = path + lb.get(lb.curselection())
    return impath

def getimage(self):
    im = Image.open(getPath())
    size = (200,200)
    im = im.resize(size)
    im = ImageTk.PhotoImage(im)
    return im

def getText():
    imtxt = getPath()[:-4] +str(".txt")
    print(imtxt)
    f = open(imtxt,'r')
    contents = f.read()
    return contents
    
def updateInfo(self):
    im = getimage(self)
    previewbox.configure(image = im)
    previewbox.image = im 
    contents = getText()
    promptbox.delete("1.0","end")
    promptbox.insert('1.0',contents)

def saveText():
    print("called")
    imtxt = getPath()[:-4] +str(".txt")

    textinput = promptbox.get(1.0, "end")
    f = open(imtxt, "w")
    f.write(textinput)
    f.close()

root = Tk()
root.title('floatme')
root.config(bg='#443644')

#Left frame for listbox and others
left_frame = Frame(root, width=200, height=200)
left_frame.grid(row=0, column=0)
left_frame.config(bg="orange")

#right frame for image previews and text editing
right_frame = Frame(root, width=200, height=200)
right_frame.grid(row=0, column=1)
right_frame.config(bg="blue")

##Listbox
lb = Listbox(left_frame, width=30, height=20, exportselection=0, selectmode="multiple")
lb.grid(row=0,column=0)

#Run getfiles once to load list of files in directory
#add a new function to insert list items I think.
getfiles()

##Box for image previews
previewbox = Label(right_frame)
previewbox.grid(row=0, column=0)

##Box for editing text
promptbox = Text(right_frame, height=8)
promptbox.grid(row=1, column=0)
testbutton = Button(left_frame,text="test", command=saveText)
testbutton.grid(row=1, column=0)
#Activate function on listbox click select 
lb.bind("<<ListboxSelect>>",updateInfo)

root.mainloop()

##TODO
#Possibly: detect for image files with no corresponding .txt files, then present button to create a file to write to.
#implement write function
##fix empty list error, not sure what is causing it directly.
###Allow for multiple selection, this might require a rework, creating a temporary array and always passing the first item from the list.
#implement batch append function <-- this should really only be for "add to selection, so if you want to add all, simply select all"
#implement find and replace 
#implement find and remove occurences

##stretch
#UI
#Prefix button
#Suffix button
#Find and remove button
#Find and replace button
#Select all button
#Open directory


