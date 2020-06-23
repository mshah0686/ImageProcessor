from tkinter import *
import numpy as np
import scipy as sc
import matplotlib as plt
from PIL import Image, ImageTk

original_image_path = "temp.gif"
choices = {'Fourier', 'LPF', 'HPF'}

#button press
def run_analysis():
    print('button pressed -> loading image')
    image = Image.open(original_image_path)
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    #save photo so garbage collector don't trash it
    label.photo = photo
    label.grid(row = 0, column = 0, pady=2)

#create application and set size
root = Tk()
root.geometry("1225x400")

#add a button
but = Button(root, command = run_analysis, text = 'Run')
but.grid(row=3, column=3, pady = 2)

#add temporary canvas for image location
var1 = IntVar()
loc1 = Canvas(root, width=300, height=300)
loc1.grid(row = 0, column = 0)
loc1.create_rectangle(0, 0, 300, 300, fill="gray")
ch1 = Checkbutton(root, text="use", var=var1).grid(row=1, column = 0)
dp1 = OptionMenu(root, None, choices)
dp1.grid(row = 2, column = 0)

var2 = IntVar()
loc2 = Canvas(root, width=300, height = 300)
loc2.grid(row = 0, column = 1)
loc2.create_rectangle(0, 0, 300, 300, fill="gray")
ch2 = Checkbutton(root, text="use", var=var2).grid(row=1, column = 1)
dp2 = OptionMenu(root, None, choices)
dp2.grid(row = 2, column = 1)

var3 = IntVar()
loc3 = Canvas(root, width=300, height = 300)
loc3.grid(row = 0, column = 2)
loc3.create_rectangle(0, 0, 300, 300, fill="gray")
ch3 = Checkbutton(root, text="use", var=var3).grid(row=1, column = 2)
dp3 = OptionMenu(root, None, choices)
dp3.grid(row = 2, column = 2)

var4 = IntVar()
loc4 = Canvas(root, width=300, height = 300)
loc4.grid(row = 0, column = 3)
loc4.create_rectangle(0, 0, 300, 300, fill="gray")
ch4 = Checkbutton(root, text="use", var=var4).grid(row=1, column = 3)
dp4 = OptionMenu(root, None, choices)
dp4.grid(row = 2, column = 3)

#run application
root.mainloop()