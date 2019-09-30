import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', required = True, help= 'Path for the image')
args = vars(ap.parse_args())


image = cv2.imread(args['i'])


def image_preprocessing(image):
	"""
	this function will take an image as input and convert it to grayscale and apply Gaussian Blurring
	it helps to remove high frequecy edges in the image
	"""
	return cv2.GaussianBlur(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), (5,5), 0)


processed = image_preprocessing(image)

# the second argument is the data type we are using 64bit float, because we need to consider both negative and positive values while talking about
# intensity change in pixels value
lap_gradient = cv2.Laplacian(processed, cv2.CV_64F)

# converting back the dtype to 8bit unsigned integer
lap_gradient = np.uint8(np.absolute(lap_gradient))



# Sobel Edge Detection
# finding edges in X and Y direction. For X direction last two arguments should be 1, 0. For Y direction 0, 1.
sob_gradient_x = cv2.Sobel(processed, cv2.CV_64F, 1, 0)
sob_gradient_Y = cv2.Sobel(processed, cv2.CV_64F, 0, 1)

#converting back dtype tp 8bit unsigned integer
sob_gradient_x = np.uint8(np.absolute(sob_gradient_x))
sob_gradient_Y = np.uint8(np.absolute(sob_gradient_Y))

# combining them to get whole edeges in Image
sob_gradient = cv2.bitwise_or(sob_gradient_x, sob_gradient_Y)

cv2.imshow('Original', image)
cv2.imshow('Processed', processed)
cv2.imshow('Laplacian', lap_gradient)
cv2.imshow('Sobel X', sob_gradient_x)
cv2.imshow('Sobel Y', sob_gradient_Y)
cv2.imshow('Sobel', sob_gradient)

cv2.waitKey(0)