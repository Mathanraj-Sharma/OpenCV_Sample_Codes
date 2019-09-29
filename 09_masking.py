import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument('-i', required= True, help = 'Path to the Image')
args = vars(ap.parse_args())

image = cv2.imread(args['i'])

def rectangluarMask(image):
	"""
	this function will take an image as an input and created a rectangluar mask(image sized) and in the center of canvas
	"""
	mask = np.zeros(image.shape[:2], dtype = 'uint8')
	(cX, cY) = (image.shape[1]//2, image.shape[0]//2)
	cv2.rectangle(mask, (cX-75, cY-75), (cX+75, cY+75), 255, -1)
	# cv2.imshow('Rectangle Mask', mask)
	# cv2.waitKey(0)
	return mask

def circleMask(image):
	"""
	this function will take an image as an input and created a circular mask(image sized) and in the center of canvas 
	with radius 100px
	"""
	mask = np.zeros(image.shape[:2], dtype = 'uint8')
	(cX, cY) = (image.shape[1]//2, image.shape[0]//2)
	cv2.circle(mask, (cX, cY), 100, 255, -1)
	# cv2.imshow('Circle Mask', mask)
	# cv2.waitKey(0)
	return mask

if __name__ == '__main__':

	cv2.imshow('Original', image)
	cv2.waitKey(0)

	rectangle_masked = cv2.bitwise_and(image, image, mask= rectangluarMask(image))
	cv2.imshow('Rectangle Masked', rectangle_masked)
	cv2.waitKey(0)

	circle_masked = cv2.bitwise_and(image, image, mask= circleMask(image))
	cv2.imshow('Circle Masked', circle_masked)
	cv2.waitKey(0)