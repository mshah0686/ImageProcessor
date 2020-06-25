from tkinter import *
import cv2 as cv
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import ttk
import filters

class choice:
    def __init__(self, checkbox, selection, previous):  
        self.use_filter = checkbox
        self.selection = selection
        self.use_previous = previous

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
    plt.subplot(2, 5, 1), plt.imshow(original_np, "gray"), plt.title("Original Image")
    next_plot = 2
    #plt.subplot(2, 5, 2), plt.imshow(np.log(1+np.abs(fourier_np)), "gray"), plt.title("Fourier Transform")
    #plt.subplot(2, 5, 3), plt.imshow(np.log(1+np.abs(shifted_np)), "gray"), plt.title("Fourier Shifted")

    #Find analysis to use
    for f in filter_choices:
        if f.use_filter.get():
            analysis = f.selection.get()
            graph_np = None
            if analysis == 'LPF':
                print('using lpf')
                graph_np = shifted_np * filters.idealFilterLP(10, original_np.shape)
            elif analysis == 'HPF':
                print('using hpf')
                graph_np = shifted_np * filters.idealFilterHP(10, original_np.shape)
            elif analysis == 'Fourier':
                print('using fourier')
                graph_np = shifted_np
            else:
                print('Nothing')
            plt.subplot(2, 5, next_plot), plt.imshow(np.log(1+np.abs(graph_np)), "gray"), plt.title(analysis)
        next_plot = next_plot + 1
    plt.show()

next_loc = 1

def add_filter():
    global filter_choices, root, next_loc
    var = IntVar()
    var2 = IntVar()
    stringvar = StringVar()
    filter_choices.append( choice(var, stringvar, var2) )
    Checkbutton(root, text="use", var=var).grid(row=0, column = next_loc)
    Checkbutton(root, text="use previous image", var = var2).grid(row = 2, column = next_loc)
    dp = ttk.Combobox(root, state="readonly", textvariable = stringvar, value=choices)
    dp.grid(row = 1, column = next_loc)
    next_loc = next_loc + 1
    print('Add fliter')

#create application and set size
root = Tk()
root.geometry("1200x100")

#add a button
but = Button(root, command = run_analysis, text = 'Analyze')
but.grid(row=0, column=0, pady = 2)
but = Button(root, command = add_filter, text = 'Add')
but.grid(row=1, column=0, pady = 2)

#run application
root.mainloop()