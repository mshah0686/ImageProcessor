from tkinter import *
import cv2 as cv
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import ttk
import filters

class choice:
    def __init__(self, checkbox, selection, previous, param):  
        self.use_filter = checkbox
        self.selection = selection
        self.use_previous = previous
        self.param = param
        self.image = None
    def setImage(self, image):
        self.image = image

original_image_path = "temp.jpg"
choices = ("Fourier", "Fourier Zero Shifted", "Ideal LPF", "Ideal HPF", "Gaussian LPF", "Gaussian HPF")
filter_choices = []

# Add option to upload an image or use default image
# Add edge detection choices
# Add using previous image checkbox functionality
# Add compression filters -> lossless and lossy

# Run analysis button function -> display the analysis on matplotlib
def run_analysis():
    global label, root, filter_choices
    print('button pressed -> loading image')
    input_np = cv.imread(original_image_path, 0)
    total_filters = 1
    for f in filter_choices:
        total_filters += f.use_filter.get()
    next_plot = 0

    #Find analysis to use
    for i in range(len(filter_choices)):
        f = filter_choices[i]
        #use if filter being applied
        if f.use_filter.get():
            original_np= []
            if f.use_previous.get() and i >0:
                original_np = filter_choices[i-1].image
            else:
                original_np = input_np
            #calculuate fourier and shifts
            fourier_np = np.fft.fft2(original_np)
            shifted_np = np.fft.fftshift(fourier_np)
            analysis = f.selection.get()

            #Scaled image radius based on image size
            scaled_size = (f.param.get() / 200) * original_np.shape[0]

            if analysis == 'Ideal LPF':
                #LOW PASS FILTER: Original, fourier, Fourier shift, LPF mask, Inverse
                graph_np = shifted_np * filters.idealFilterLP(scaled_size, original_np.shape)
                spatial_image = np.fft.ifft2(graph_np)
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.imshow(np.log(1+np.abs(fourier_np)), "gray"), plt.title('fourier')
                plt.subplot(total_filters, 5, next_plot * 5 + 3), plt.imshow(np.log(1+np.abs(shifted_np)), "gray"), plt.title('zero shift')
                plt.subplot(total_filters, 5, next_plot * 5 + 4), plt.imshow(np.log(1+np.abs(graph_np)), "gray"), plt.title('mask')
                plt.subplot(total_filters, 5, next_plot * 5 + 5), plt.imshow(np.log(1+np.abs(spatial_image)), "gray"), plt.title('LPF')
                f.image = np.log(1+np.abs(spatial_image))
            elif analysis == 'Ideal HPF':
                #HIGH PASS FILTER: Original, fourier, Fourier shift, HPF mask, Inverse
                graph_np = shifted_np * filters.idealFilterHP(scaled_size, original_np.shape)
                spatial_image = np.fft.ifft2(graph_np)
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.imshow(np.log(1+np.abs(fourier_np)), "gray"), plt.title('fourier')
                plt.subplot(total_filters, 5, next_plot * 5 + 3), plt.imshow(np.log(1+np.abs(shifted_np)), "gray"), plt.title('zero shift')
                plt.subplot(total_filters, 5, next_plot * 5 + 4), plt.imshow(np.log(1+np.abs(graph_np)), "gray"), plt.title('mask')
                plt.subplot(total_filters, 5, next_plot * 5 + 5), plt.imshow(np.log(1+np.abs(spatial_image)), "gray"), plt.title('HPF')
                f.image = np.log(1+np.abs(spatial_image))
            
            elif analysis == 'Gaussian LPF':
                #Gaussian LPF: Original, fourier, Fourier Shift, Mask, Inverse
                graph_np = shifted_np * filters.gaussianLP(scaled_size, original_np.shape)
                spatial_image = np.fft.ifft2(graph_np)
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.imshow(np.log(1+np.abs(fourier_np)), "gray"), plt.title('fourier')
                plt.subplot(total_filters, 5, next_plot * 5 + 3), plt.imshow(np.log(1+np.abs(shifted_np)), "gray"), plt.title('zero shift')
                plt.subplot(total_filters, 5, next_plot * 5 + 4), plt.imshow(np.log(1+np.abs(graph_np)), "gray"), plt.title('mask')
                plt.subplot(total_filters, 5, next_plot * 5 + 5), plt.imshow(np.log(1+np.abs(spatial_image)), "gray"), plt.title('Gaussian LPF')
                f.image = np.log(1+np.abs(spatial_image))
            
            elif analysis == 'Gaussian HPF':
                #Gaussian HPF: Original, fourier, Fourier Shift, Mask, Inverse
                graph_np = shifted_np * filters.gaussianHP(scaled_size, original_np.shape)
                spatial_image = np.fft.ifft2(graph_np)
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.imshow(np.log(1+np.abs(fourier_np)), "gray"), plt.title('fourier')
                plt.subplot(total_filters, 5, next_plot * 5 + 3), plt.imshow(np.log(1+np.abs(shifted_np)), "gray"), plt.title('zero shift')
                plt.subplot(total_filters, 5, next_plot * 5 + 4), plt.imshow(np.log(1+np.abs(graph_np)), "gray"), plt.title('mask')
                plt.subplot(total_filters, 5, next_plot * 5 + 5), plt.imshow(np.log(1+np.abs(spatial_image)), "gray"), plt.title('Gaussian HPF')
                f.image = np.log(1+np.abs(spatial_image))
            
            elif analysis == 'Fourier':
                #Fourier
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.imshow(np.log(1+np.abs(fourier_np)), "gray"), plt.title('fourier')
                f.image = original_np
            
            elif analysis == 'Fourier Zero Shifted':
                #Fourier, zero shift
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.imshow(np.log(1+np.abs(fourier_np)), "gray"), plt.title('fourier')
                plt.subplot(total_filters, 5, next_plot * 5 + 3), plt.imshow(np.log(1+np.abs(shifted_np)), "gray"), plt.title('zero shift')
                f.image = origional_np
            
            elif analysis == 'Edge Detection':
                #TODO: implement edge detection
                pass
            
            elif analysis == 'Compression':
                pass
        next_plot = next_plot + 1
    plt.show()
next_loc = 1

# Adding filter option to the window
def add_filter():
    global filter_choices, root, next_loc
    #Variables per filter
    var = IntVar(value=1)
    var2 = IntVar(value=1)
    stringvar = StringVar()
    param = IntVar(value = 25)

    #add filter to array as choice object
    filter_choices.append( choice(var, stringvar, var2, param) )

    #Add check box for applying filter or not
    Checkbutton(root, text="Apply Filter", var=var).grid(row=0, column = next_loc)

    #Combobox for filter choices
    dp = ttk.Combobox(root, state="readonly", textvariable = stringvar, value=choices)
    dp.grid(row = 1, column = next_loc)

    #Add check box for using previous or original
    Checkbutton(root, text="Use Previous Filter as Input", var = var2).grid(row = 2, column = next_loc)

    #Input for parameter selection
    slider = Scale(from_=0, to=100, resolution=0.1, label="Size(%)(if applicable):", orient=HORIZONTAL, length=145, variable = param)
    slider.grid(row = 3, column = next_loc)

    #Update location
    next_loc = next_loc + 1
    print('Add fliter')

#create application and set size
root = Tk()
root.geometry("1200x150")

#add a button
but = Button(root, command = run_analysis, text = 'Analyze')
but.grid(row=0, column=0, pady = 2)
but = Button(root, command = add_filter, text = 'Add')
but.grid(row=1, column=0, pady = 2)

#run application
root.mainloop()