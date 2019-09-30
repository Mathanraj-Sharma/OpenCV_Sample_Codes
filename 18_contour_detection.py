import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument('-i', required = True, help = 'Path to the image')
args = vars(ap.parse_args())


image = cv2.imread(args['i'])

# to detect the shape first we need to detect the edges below function will do that
def edge_detect(image):
	"""
	this function will get an image as an input convert it to grayscale apply Gaussian Blurring and Canny Edge detection 
	then it will return the output image
	"""
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gau_blurred = cv2.GaussianBlur(gray_image,(5,5),0)
	return cv2.Canny(gau_blurred, 30, 150)


edged = edge_detect(image)

# (_ ,cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

copy_image = image.copy()
cv2.drawContours(copy_image, cnts, -1, (0,255,0),2)

cv2.imshow('Original', image)
cv2.imshow('Contour', copy_image)
cv2.waitKey(0)
