from tkinter import filedialog
from tkinter import *
import os
from os.path import isfile, isdir

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    folder_path.set(os.getcwd())
    print(folder_path)
    dir = os.listdir()

    for d in dir:
    	if isfile(d):
    		print(d + " is a file")
    	elif isdir(d):
    		print(d + " is a directory")
    		dir = os.chdir()
    		print(dir)
    		break


root = Tk()
folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=0, column=3)

mainloop()