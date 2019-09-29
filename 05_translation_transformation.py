import cv2
import numpy as np
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('-i','-image',   required = True, help = 'Enter the path for the image')
args = vars(ap.parse_args())

image = cv2.imread(args['i'])


def translate(image, tx, ty):
	"""
	This function will create a translation matrix using tx, ty and return a translated image
	think interms of matrix multiplication for translation
	--      --   -- --
	| 1 0 tx |   | x |
	| 0 1 ty | * | y |
	| 0 0 1  |   | 1 |
	--      --   -- --
	"""
	M = np.float32([[1,0,tx], [0,1,ty]])
	translated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
	return translated_image


if __name__ == '__main__':
	cv2.imshow('Original Image', image)
	cv2.waitKey(0)

	test_translation = translate(image, 50, 100)
	cv2.imshow('Translated Image', test_translation)
	cv2.waitKey(0)

	""" 
		Since the origin of image is on the left top corner
		
		Negative value for ty will move the image up
		Positive value for ty will move the image down

		Negative value for tx will move the image left
		Positive value for tx will move the image right
	"""
