import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt


ap = argparse.ArgumentParser()
ap.add_argument('-i', required = True, help = 'Path to Image')
args = vars(ap.parse_args())

image = cv2.imread(args['i'])

# grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def gen_hist(image, title, fig_number):
	"""
	this function will get a gray scale image as an input and generates it histogram
	"""
	cv2.imshow(title, image)
	cv2.waitKey(0)
	hist = cv2.calcHist([image],[0], None, [256], [0,256])

	_ = plt.figure(fig_number)
	_ = plt.title(title)
	_ = plt.xlabel('Bins from 0 - 255')
	_ = plt.ylabel('# of pixels')
	_ = plt.plot(hist)
	_ = plt.xlim([0,256])
	
	
	

if __name__ == '__main__':

	gen_hist(grayScale, "Before Equalization", 1)

	#equalization function
	eq = cv2.equalizeHist(grayScale)

	gen_hist(eq, 'After equalization', 2)
	
	plt.show()

