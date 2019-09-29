import cv2
import numpy as np
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('-i', required = True, help= 'Path for the image')
args = vars(ap.parse_args())


image = cv2.imread(args['i'])


"""
image thresholding is a task that convert the values of pixels
-less than the given value to 0
-greater than the given value to 255
"""

def image_preprocessing(image):
	"""
	this function will take an image as input and convert it to grayscale and apply Gaussian Blurring
	it helps to remove high frequecy edges in the image, which will give smooth thresholding
	"""
	return cv2.GaussianBlur(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), (5,5), 0)


processed = image_preprocessing(image)

(T, thresh) = cv2.threshold(processed, 155, 255, cv2.THRESH_BINARY)
"""
T - the threshold value we given 155
1st argument the image
2nd argument the threshold value 155
3rd argument the maximum value that has to be assigned to the pixels greater than threshold value
4th argument the conversion cv2.THRESH_BINARY or cv2.THRESH_BINARY_INV
"""


(T, thresh_inv) = cv2.threshold(processed, 155, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('Orginal Image', image)
cv2.imshow('Thresholded Image', thresh)
cv2.imshow('Inversly Thresholded Image', thresh_inv)

cv2.waitKey(0)