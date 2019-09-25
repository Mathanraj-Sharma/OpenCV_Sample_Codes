import cv2
import numpy as np

canvas = np.zeros((300,300,3), dtype = 'uint8')

def drawCircle(center, radius, color, width):
	""" 
	this function will draw a circle for given center point and radius
	Here center is a tuple of coordinates, if you pass -1 for width
	it will give a filled circle
	"""
	cv2.circle(canvas, center, radius, color, width)


if __name__ == '__main__':

	center = (150,150)
	radius = 100
	green = (0,255,0)
	width = 2

	drawCircle(center, radius, green, width)
	cv2.imshow('Circle Canvas', canvas)
	cv2.waitKey(0)

	drawCircle(center, radius, green, -1)
	cv2.imshow('Circle Canvas', canvas)
	cv2.waitKey(0)

