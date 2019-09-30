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



"""
In Canny edge detection we will pass two threshold values t1 ,t2

pixel value > t2  => considered as an edge
pixel value < t1  => considered as not an edge
t1 < pixel value < t2 => may or maynot an edge it has to be decided by the algorithm it self (if steep intensity change exists then edge or not)
"""

processed = image_preprocessing(image)

canny_edge = cv2.Canny(processed, 30, 150)

cv2.imshow('Original', image)
cv2.imshow('Processed', processed)
cv2.imshow('Canny Edge', canny_edge)

cv2.waitKey(0)