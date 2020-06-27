import cv2 as cv
import numpy as np
import scipy.ndimage as sp
import matplotlib.pyplot as plt

def sobel_edge(image):
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.transpose(sobel_x)
    #img = image.flatten()
    #sobel_filter = sobel.flatten()
    x_img = sp.convolve(image, sobel_x, mode='constant', cval=0.0)
    y_img = sp.convolve(image, sobel_y, mode='constant', cval=0.0)
    plt.imshow(y_img, 'gray')
    plt.show()

input_np = cv.imread('temp.jpg', 0)
sobel_edge(input_np)


