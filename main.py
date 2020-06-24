from tkinter import *
import cv2
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import ttk 

original_image_path = "temp.jpg"
choices = ("Fourier", "LPF", "HPF")
check_box_var = {}
analysis_selection = {}

#button press
def run_analysis():
    global label, root
    print('button pressed -> loading image')
    original_np = cv2.imread(original_image_path, 0)
    fourier_np = np.fft.fft2(original_np)

    #fourier_TK = Image.fromarray((fourier_np * 255).astype(np.uint8))
    fourier_TK = Image.fromarray((fourier_np * 255).astype(np.uint8))
    fourier_TK = ImageTk.PhotoImage(fourier_TK)
    temp = Canvas(root,width=300,height=300)
    temp.grid(row = 0, column = 1)
    temp.create_image(image=fourier_TK)

    temp.photo = fourier_TK
    temp.grid(row=0, column = 1)

#create application and set size
root = Tk()
root.geometry("1225x400")

#add a button
but = Button(root, command = run_analysis, text = 'Analyze')
but.grid(row=3, column=3, pady = 2)

#add temporary canvas for image location
#Original image location
#var1 = IntVar()
loc1 = Canvas(root, width=300, height=300)
loc1.grid(row = 0, column = 0)
loc1.create_rectangle(0, 0, 300, 300, fill="gray")
#ch1 = Checkbutton(root, text="use", var=var1).grid(row=1, column = 0)
#dp1 = OptionMenu(root, None, choices)
#dp1.grid(row = 2, column = 0)

#Load and display image
image = Image.open(original_image_path)
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
#save photo so garbage collector don't trash it
label.photo = photo
label.grid(row = 0, column = 0, pady=2)

var2 = IntVar()
stringVar2 = StringVar()
loc2 = Canvas(root, width=300, height = 300)
loc2.grid(row = 0, column = 1)
loc2.create_rectangle(0, 0, 300, 300, fill="gray")
Checkbutton(root, text="use", var=var2).grid(row=1, column = 1)
dp2 = ttk.Combobox(root, state="readonly", textvariable = stringVar2, value=choices)
dp2.grid(row = 2, column = 1)

var3 = IntVar()
stringVar3 = StringVar()
loc3 = Canvas(root, width=300, height = 300)
loc3.grid(row = 0, column = 2)
loc3.create_rectangle(0, 0, 300, 300, fill="gray")
Checkbutton(root, text="use", var=var3).grid(row=1, column = 2)
dp3 = ttk.Combobox(root, state="readonly", textvariable = stringVar3, value=choices)
dp3.grid(row = 2, column = 2)

var4 = IntVar()
stringVar4 = StringVar()
loc4 = Canvas(root, width=300, height = 300)
loc4.grid(row = 0, column = 3)
loc4.create_rectangle(0, 0, 300, 300, fill="gray")
Checkbutton(root, text="use", var=var4).grid(row=1, column = 3)
dp4 = ttk.Combobox(root, state="readonly", textvariable = stringVar4, value=choices)
dp4.grid(row = 2, column = 3)

#run application
root.mainloop()