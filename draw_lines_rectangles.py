import cv2
import numpy as np

#defining a canvas with 300*300 pixels with 3 channels
canvas = np.zeros((300,300,3), dtype = 'uint8')

def drawLine(start, end, color, width):
	"""
		this function will draw a line from start pixel to ending pixel
		Here start and end are tuples of coordinate values
	"""
	cv2.line(canvas, start, end, color, width)


def draw_rectangle(start, end, color, width):
	"""
		this function will draw a rectangle from start pixel to ending pixel
		Here start and end are tuples of coordinate values
		Passing -1 for width will give filled rectangle
	"""
	cv2.rectangle(canvas, start, end, color, width)


if __name__ == '__main__':
	start = (0,0)
	end = (300,300)
	green = (0,255,0) #green


	drawLine(start, end, green,1)
	drawLine((300,0), (0,300), (255,0,0),5 )
	cv2.imshow('My Canvas', canvas)
	cv2.waitKey(0)


	draw_rectangle((10,10), (50,50), (0,0,255), 2)
	draw_rectangle((125,125), (250,250), (255,0,255), -1)
	cv2.imshow('Rectangle Canvas', canvas)
	cv2.waitKey(0)

