from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv
from skimage import exposure

def image_histogram_equalization(image, number_bins=256):
    # get image histogram
    image_histogram, bins = np.histogram(image.flatten(), number_bins, density=True)
    cdf = image_histogram.cumsum() # cumulative distribution function
    normalized_cdf = 255 * cdf / cdf[-1] # normalize
    
    # use linear interpolation of cdf to find new pixel values
    image_equalized = np.interp(image.flatten(), bins[:-1], normalized_cdf)
    plt.subplot(1, 5, 1), plt.plot(cdf)
    plt.subplot(1, 5, 2), plt.hist(image_histogram)
    plt.subplot(1, 5, 3), plt.plot(normalized_cdf)
    #plt.subplot(1, 5, 4), plt.imshow(image_equalized.reshape(image.shape))
    #plt.show()
    return image_equalized.reshape(image.shape), normalized_cdf

def histogram_equalize(img):
    img_cdf, bin_centers = exposure.cumulative_distribution(img)
    return np.interp(img, bin_centers, img_cdf)

if __name__ == '__main__':
    image = cv.imread('temp.jpg', 0)
    result,temp= image_histogram_equalization(image)
    plt.hist(temp)
    plt.show()