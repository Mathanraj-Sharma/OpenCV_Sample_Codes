# cv2.calcHist(image, channels, mask, histSize, ranges)

# image - the image we want to make histogram
# channel - the index of the channel we want to built hist for, for grayscale image [0], for full RGB image [0,1,2]
# mask - if we want to cal hist for a region of interest pass the mask
# histSize - number of bins
# ranges - range of possible pixel values normally [0,256] - will give  0-255

import matplotlib.pyplot as plt
import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument('-i', required = True, help = 'Path to the Image')
args = vars(ap.parse_args())

image = cv2.imread(args['i'])

def grayScaleHist(image):
	"""
	this function will convert color image into grayscale and show the histogram for that grayscale image
	"""

	gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cv2.imshow('Grayscale Image', gray_scale)

	hist = cv2.calcHist([gray_scale],[0], None, [256], [0,256])

	_ = plt.figure()
	_ = plt.title('Grayscale Histogram')
	_ = plt.xlabel('Bins from 0 - 255')
	_ = plt.ylabel('# of pixels')
	_ = plt.plot(hist)
	_ = plt.xlim([0,256])

	plt.show()
	cv2.waitKey(0)

def rgbHist(image):
	"""
	this function will take an image as input and display its histogram
	"""
	cv2.imshow('Color Image', image)
	histB = cv2.calcHist([image],[0], None, [256], [0,256])
	histG = cv2.calcHist([image],[1], None, [256], [0,256])
	histR = cv2.calcHist([image],[2], None, [256], [0,256])

	_ = plt.figure()
	_ = plt.title('RGB Histogram')
	_ = plt.xlabel('Bins from 0 - 255')
	_ = plt.ylabel('# of pixels')
	_ = plt.plot(histB, color = 'blue')
	_ = plt.plot(histG, color = 'green')
	_ = plt.plot(histR, color = 'red')
	_ = plt.xlim([0,256])

	plt.show()
	cv2.waitKey(0)


if __name__ == '__main__':
	#grayScaleHist(image)
	rgbHist(image)