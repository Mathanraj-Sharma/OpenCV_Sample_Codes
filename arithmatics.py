import cv2
import numpy as np
import argparse

"""
print('OpenCV perform Clipping when underflow or overflow occur in pixel values...')
print(f'OpenCV Addition of 200 + 100 = {cv2.add(np.uint8([200]),np.uint8([100]))}')
print(f'OpenCV Substraction of 50 - 100 = {cv2.subtract(np.uint8([50]),np.uint8([100]))}')

print('\nNumpy perform wrap Around when underflow or overflow occure in pixel values...')

print(f'numpy Addition of 200 + 100 = {np.add(np.uint8([200]),np.uint8([100]))}')
print(f'numpy Substraction of 50 - 100 = {np.subtract(np.uint8([50]),np.uint8([100]))}')
"""


ap = argparse.ArgumentParser()
ap.add_argument('-i', required = True, help = 'Path to the Image')
args = vars(ap.parse_args())


image = cv2.imread(args['i'])

def add_to_image(image, value):
	"""
	this function will add given value to all the pixels in given image, 
	"""
	M = np.ones(image.shape, dtype = 'uint8') * value
	added_image = cv2.add(image, M)
	return added_image

def sub_from_image(image, value):
	"""
	this function will subtract given value from all the pixels in given image, 
	"""
	M = np.ones(image.shape, dtype = 'uint8') * value
	subbed_image = cv2.subtract(image, M)
	return subbed_image


if __name__ == '__main__':

	cv2.imshow('Original', image)
	cv2.waitKey(0)

	added_100 = add_to_image(image, 100)
	cv2.imshow('Added 100', added_100)
	cv2.waitKey(0)

	subbed_100 = sub_from_image(image, 100)
	cv2.imshow('Subbed 100', subbed_100)
	cv2.waitKey(0)


