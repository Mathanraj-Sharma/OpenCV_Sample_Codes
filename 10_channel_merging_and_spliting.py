import cv2
import numpy as np
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('-i', required = True, help = 'Path to the Image')
args = vars(ap.parse_args())

image = cv2.imread(args['i'])


def split_chennels(image):
	"""
	this function will an image as an input and splits its channels
	"""
	zeros = np.zeros(image.shape[:2], dtype='uint8')
	(B, G, R) = cv2.split(image)

	#we merge and build channels to visualize theri actuals colors. if you imshow B, G, R it will be three graycale images

	# cv2.imshow('RED', R)
	# cv2.imshow('GREEN', G)
	# cv2.imshow('BLUE', B)

	cv2.imshow('RED', cv2.merge([zeros, zeros, R]))
	cv2.imshow('GREEN', cv2.merge([zeros, G, zeros]))
	cv2.imshow('BLUE', cv2.merge([B, zeros, zeros]))
	cv2.waitKey(0)

if __name__ == '__main__':

	cv2.imshow('Orginal RGB image', image)
	cv2.waitKey(0)

	split_chennels(image)