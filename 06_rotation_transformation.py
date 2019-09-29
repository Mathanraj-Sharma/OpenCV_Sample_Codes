import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument('-i', required = True, help = 'Enter the path of Image')
args = vars(ap.parse_args())

image = cv2.imread(args['i'])

def wheel(image, center):
	i = 1
	while (True):
		if i > 359:
			cv2.imshow('Wheel', image)
			cv2.waitKey(1)
			i = 1
		else:
			rotated_image = rotate(image, center, i, 1.0)
			cv2.imshow('Wheel', rotated_image)
			cv2.waitKey(10)
			i += 1


def rotate(image, point, angle, scale):
	"""
	this function will take an image and rotate it through the given angle
	with respect to given point.

	Optionally we can scale the image 1.0 = original, 2.0 = double etc.
	"""

	# M is the rotation Matrix for derived using angel, Point, and Scale
	M = cv2.getRotationMatrix2D(point, angle, scale)
	rotated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
	return rotated_image


if __name__ == '__main__':

	#tranforming image with respect to its center and through -45*

	center = (image.shape[1]//2, image.shape[0]//2)
	angel = -45

	cv2.imshow('Original Image', image)
	cv2.waitKey(0)

	rotated_image = rotate(image, center, angel, 1.0)

	cv2.imshow('Rotated Image', rotated_image)
	cv2.waitKey(0)
	

	wheel(image, center)