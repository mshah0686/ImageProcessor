from tkinter import *
import cv2 as cv
import numpy as np
import scipy.ndimage as sp
import math
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import ttk
import filters
import argparse

#Filter object -> created upon button click
class choice:
    def __init__(self, checkbox, selection, previous, param):  
        self.use_filter = checkbox
        self.selection = selection
        self.use_previous = previous
        self.param = param
        self.image = None

original_image_path = "temp.jpg"
choices = ("Fourier", "Fourier Zero Shifted", "Ideal LPF", "Ideal HPF", 
            "Gaussian LPF", "Gaussian HPF", 
            "Intensity Inverse", "Intensity Quantize", "Gaussian Blur", "Flat Filter", "Histogram Equalization",
            "Sobel Gradient Combined", "Sobel Horizontal Gradient", "Sobel Vertical Gradient", "Laplacian")
filter_choices = []

#TODO LIST
# Add option to upload an image or use default image
# Add compression filters -> lossless and lossy
# Dynamic quantization
# Help button for details on each filter

# Run analysis button function -> display the analysis on matplotlib
def run_analysis():
    global label, root, filter_choices
    input_np = cv.imread(original_image_path, 0)
    total_filters = 1
    sorted_choices = []

    # Make a new array of the filters that need to be used
    for f in filter_choices:
        if f.use_filter.get():
            sorted_choices.append(f)
    next_plot = 0
    total_filters = len(sorted_choices)

    #Run through filters and apply analysis
    for i in range(len(sorted_choices)):
        f = sorted_choices[i]

        #use if filter being applied
        if f.use_filter.get():
            original_np= []
            if f.use_previous.get() and i >0:
                original_np = sorted_choices[i-1].image
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
                spatial_image = filters.inverseFFT(np.fft.ifft2(graph_np))
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.imshow(np.log(1+np.abs(fourier_np)), "gray"), plt.title('fourier')
                plt.subplot(total_filters, 5, next_plot * 5 + 3), plt.imshow(np.log(1+np.abs(shifted_np)), "gray"), plt.title('zero shift')
                plt.subplot(total_filters, 5, next_plot * 5 + 4), plt.imshow(np.log(1+np.abs(graph_np)), "gray"), plt.title('mask')
                plt.subplot(total_filters, 5, next_plot * 5 + 5), plt.imshow(spatial_image, "gray"), plt.title('LPF')
                f.image = spatial_image

            elif analysis == 'Ideal HPF':
                #HIGH PASS FILTER: Original, fourier, Fourier shift, HPF mask, Inverse
                graph_np = shifted_np * filters.idealFilterHP(scaled_size, original_np.shape)
                spatial_image = filters.inverseFFT(np.fft.ifft2(graph_np))
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.imshow(np.log(1+np.abs(fourier_np)), "gray"), plt.title('fourier')
                plt.subplot(total_filters, 5, next_plot * 5 + 3), plt.imshow(np.log(1+np.abs(shifted_np)), "gray"), plt.title('zero shift')
                plt.subplot(total_filters, 5, next_plot * 5 + 4), plt.imshow(np.log(1+np.abs(graph_np)), "gray"), plt.title('mask')
                plt.subplot(total_filters, 5, next_plot * 5 + 5), plt.imshow(spatial_image, "gray"), plt.title('HPF')
                f.image = spatial_image
            
            elif analysis == 'Gaussian LPF':
                #Gaussian LPF: Original, fourier, Fourier Shift, Mask, Inverse
                graph_np = shifted_np * filters.gaussianLP(scaled_size, original_np.shape)
                spatial_image = filters.inverseFFT(np.fft.ifft2(graph_np))
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.imshow(np.log(1+np.abs(fourier_np)), "gray"), plt.title('fourier')
                plt.subplot(total_filters, 5, next_plot * 5 + 3), plt.imshow(np.log(1+np.abs(shifted_np)), "gray"), plt.title('zero shift')
                plt.subplot(total_filters, 5, next_plot * 5 + 4), plt.imshow(np.log(1+np.abs(graph_np)), "gray"), plt.title('mask')
                plt.subplot(total_filters, 5, next_plot * 5 + 5), plt.imshow(spatial_image, "gray"), plt.title('Gaussian LPF')
                f.image = spatial_image
            
            elif analysis == 'Gaussian HPF':
                #Gaussian HPF: Original, fourier, Fourier Shift, Mask, Inverse
                graph_np = shifted_np * filters.gaussianHP(scaled_size, original_np.shape)
                spatial_image = filters.inverseFFT(np.fft.ifft2(graph_np))
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.imshow(np.log(1+np.abs(fourier_np)), "gray"), plt.title('fourier')
                plt.subplot(total_filters, 5, next_plot * 5 + 3), plt.imshow(np.log(1+np.abs(shifted_np)), "gray"), plt.title('zero shift')
                plt.subplot(total_filters, 5, next_plot * 5 + 4), plt.imshow(np.log(1+np.abs(graph_np)), "gray"), plt.title('mask')
                plt.subplot(total_filters, 5, next_plot * 5 + 5), plt.imshow(spatial_image, "gray"), plt.title('Gaussian HPF')
                f.image = spatial_image
            
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
                f.image = original_np
            
            elif analysis == 'Intensity Inverse':
                #Transformation => T(x) = 255 - f
                transformed = np.copy(original_np)
                for i in range(original_np.shape[0]):
                    for j in range(original_np.shape[1]):
                        transformed[i][j] = 255 - original_np[i][j]
                #Transform graph
                x = np.array(range(0,255))
                y = eval('255-x')
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.plot(x,y), plt.title('pixel transform')
                plt.subplot(total_filters, 5, next_plot * 5 + 3), plt.imshow(transformed, "gray"), plt.title('inverse')
                f.image = transformed
            
            elif analysis == 'Intensity Quantize':
                #number of bits to quantize
                levels = int(f.param.get())
                transformed = np.copy(original_np)
                delta = 256 / levels
                for i in range(original_np.shape[0]):
                    for j in range(original_np.shape[1]):
                        val = original_np[i][j]
                        #print(val)
                        transformed[i][j] = math.floor( (val/delta) + 0.5) * delta
                #transform graph
                x = np.array(range(0,255))
                y = np.floor( (x/delta) + 0.5) * delta
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.plot(x,y), plt.title('pixel transform')
                plt.subplot(total_filters, 5, next_plot * 5 + 3), plt.imshow(transformed, "gray"), plt.title('quantized')
                f.image = transformed
            
            elif analysis == 'Sobel Gradient Combined':
                x_img, y_img= filters.sobel_edge(original_np)
                combined = np.array(np.sqrt((x_img **2) + (y_img **2)), dtype='uint8')
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.imshow(x_img, "gray"), plt.title('sobel x gradient')
                plt.subplot(total_filters, 5, next_plot * 5 + 3), plt.imshow(y_img, "gray"), plt.title('sobel y gradient')
                plt.subplot(total_filters, 5, next_plot * 5 + 4), plt.imshow(combined, "gray"), plt.title('combined')
                f.image = combined
            
            elif analysis == 'Sobel Horizontal Gradient':
                x_img, _ = filters.sobel_edge(original_np)
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.imshow(x_img, "gray"), plt.title('sobel x gradient')
                f.image = x_img
            
            elif analysis == 'Sobel Vertical Gradient':
                _, y_img= filters.sobel_edge(original_np)
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.imshow(y_img, "gray"), plt.title('sobel y gradient')
                f.image = y_img
            
            elif analysis == 'Laplacian':
                laplace = filters.laplace_filter(original_np)
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.imshow(laplace, "gray"), plt.title('laplace edge')
                f.image = laplace

            elif analysis == 'Gaussian Blur':
                sigma = int(f.param.get())
                blurred = filters.gaussian_blur(original_np, sigma)
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.imshow(blurred, "gray"), plt.title('gaussian blur')
                f.image = blurred
            
            elif analysis == 'Histogram Equalization':
                normalized, histogram,_,_ = filters.histogram_equalization(original_np, 256)
                new_histogram, _ = np.histogram(normalized.flatten(), 256, density=True)
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.hist(histogram), plt.title('original histogram')
                plt.subplot(total_filters, 5, next_plot * 5 + 3), plt.hist(new_histogram),  plt.title('normailized histogram')
                plt.subplot(total_filters, 5, next_plot * 5 + 4), plt.imshow(normalized, "gray"), plt.title('normalized')
                f.image = normalized

            elif analysis == 'Flat Filter':
                flat_fitered = filters.flat_filter(original_np)
                plt.subplot(total_filters, 5, next_plot * 5 + 1), plt.imshow(original_np, "gray"), plt.title('original')
                plt.subplot(total_filters, 5, next_plot * 5 + 2), plt.imshow(flat_fitered, "gray"),  plt.title('flat_filtered 3x3')
                f.image = flat_fitered
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


#get arguments for file name input
parser = argparse.ArgumentParser(description='File name')
parser.add_argument('-f', '--file', help='file path, default is temp.jpg')
args = parser.parse_args()
if args.file:
    original_image_path = args.file

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