import numpy as np
from random import *
from math import sqrt,exp
import scipy.ndimage as sp

def distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def idealFilterLP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            if distance((y,x),center) < D0:
                base[y,x] = 1
    return base

def idealFilterHP(D0,imgShape):
    base = np.ones(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            if distance((y,x),center) < D0:
                base[y,x] = 0
    return base

def randomFilter(imgShape):
    base = np.ones(imgShape[:2])
    rows, cols = imgShape[:2]
    for x in range(cols):
        for y in range(rows):
            base[y,x] = randint(0,1)
    return base

def gaussianLP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = exp(((-distance((y,x),center)**2)/(2*(D0**2))))
    return base

def gaussianHP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1 - exp(((-distance((y,x),center)**2)/(2*(D0**2))))
    return base

def inverseFFT(img):
    filtered_img = np.abs(img)
    filtered_img -= filtered_img.min()
    filtered_img = filtered_img*255 / filtered_img.max()
    filtered_img = filtered_img.astype(np.uint8)
    return filtered_img

def sobel_edge(img):
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.transpose(sobel_x)
    filters = sp.convolve(sobel_x, sobel_y, mode='constant', cval = 0.0)
    x_img = sp.convolve(img, sobel_x, mode='constant', cval=0.0)
    y_img = sp.convolve(img, sobel_y, mode='constant', cval=0.0)
    combined = sp.convolve(img, filters, mode='constant', cval=0.0)
    return x_img, y_img, combined
