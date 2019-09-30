import cv2
import numpy as np
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('-i', required = True, help= 'Path for the image')
args = vars(ap.parse_args())


image = cv2.imread(args['i'])


"""
Here the threshold value will be dynamically calculated by condsidering neighbor pixels, there are two methods to do it
Using the Averaging Threshold Kernal - ADAPTIVE_THRESH_MEAN_C
Using the Gaussian Threshold Kernal - ADAPTIVE_THRESH_GAUSSIAN_C
"""

def image_preprocessing(image):
	"""
	this function will take an image as input and convert it to grayscale and apply Gaussian Blurring
	it helps to remove high frequecy edges in the image, which will give smooth thresholding
	"""
	return cv2.GaussianBlur(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), (5,5), 0)


processed = image_preprocessing(image)

ave_thresh = cv2.adaptiveThreshold(processed, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
"""
1st argument the image
2nd argument the maximum value that has to be assigned to the pixels greater than threshold value
3rd argument the kernal to calculate threshold value
4th argument the conversion cv2.THRESH_BINARY or cv2.THRESH_BINARY_INV
5th argument the number of neighbors to be considered in kernal (kernal size)
6th argument the value to be substracted from the dynamic threshold value , allows to tune the thresholding
"""

gau_thresh = cv2.adaptiveThreshold(processed, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)

cv2.imshow('Orginal Image', image)
cv2.imshow('Average Thresholded Image', ave_thresh)
cv2.imshow('Gaussian Thresholded Image', gau_thresh)

cv2.waitKey(0)