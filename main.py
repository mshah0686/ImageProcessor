from tkinter import *
import cv2 as cv
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import ttk

class choice:
    def __init__(self, checkbox, selection):  
        self.checkbox = checkbox
        self.selection = selection

original_image_path = "temp.jpg"
choices = ("Fourier", "LPF", "HPF")
filter_choices = []

#button press
def run_analysis():
    global label, root, filter_choices
    print('button pressed -> loading image')
    original_np = cv.imread(original_image_path, 0)
    fourier_np = np.fft.fft2(original_np)
    shifted_np = np.fft.fftshift(fourier_np)
    plt.subplot(251), plt.imshow(original_np, "gray"), plt.title("Original Image")
    plt.subplot(252), plt.imshow(np.log(1+np.abs(fourier_np)), "gray"), plt.title("Fourier Transform")
    plt.subplot(253), plt.imshow(np.log(1+np.abs(shifted_np)), "gray"), plt.title("Fourier Shifted")
    for f in filter_choices:
        if f.checkbox.get():
            analysis = f.selection.get()
            print(analysis)
    plt.show()

#create application and set size
root = Tk()
root.geometry("1200x100")

#add a button
but = Button(root, command = run_analysis, text = 'Analyze')
but.grid(row=0, column=0, pady = 2)

var1 = IntVar()
stringVar1 = StringVar()
filter_choices.append( choice(var1, stringVar1) )
Checkbutton(root, text="use", var=var1).grid(row=0, column = 1)
dp1 = ttk.Combobox(root, state="readonly", textvariable = stringVar1, value=choices)
dp1.grid(row = 1, column = 1)

var2 = IntVar()
stringVar2 = StringVar()
filter_choices.append( choice(var2, stringVar2) )
Checkbutton(root, text="use", var=var2).grid(row=0, column = 2)
dp2 = ttk.Combobox(root, state="readonly", textvariable = stringVar2, value=choices)
dp2.grid(row = 1, column = 2)

var3 = IntVar()
stringVar3 = StringVar()
filter_choices.append( choice(var3, stringVar3) )
Checkbutton(root, text="use", var=var3).grid(row=0, column = 3)
dp3 = ttk.Combobox(root, state="readonly", textvariable = stringVar3, value=choices)
dp3.grid(row = 1, column = 3)

var4 = IntVar()
stringVar4 = StringVar()
filter_choices.append( choice(var4, stringVar4) )
Checkbutton(root, text="use", var=var4).grid(row=0, column = 4)
dp4 = ttk.Combobox(root, state="readonly", textvariable = stringVar4, value=choices)
dp4.grid(row = 1, column = 4)

var5 = IntVar()
stringVar5 = StringVar()
filter_choices.append( choice(var5, stringVar5) )
Checkbutton(root, text="use", var=var5).grid(row=0, column = 5)
dp5 = ttk.Combobox(root, state="readonly", textvariable = stringVar5, value=choices)
dp5.grid(row = 1, column = 5)

#run application
root.mainloop()