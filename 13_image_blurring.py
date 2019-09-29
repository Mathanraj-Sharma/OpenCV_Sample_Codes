import cv2
import numpy as np
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('-i', required = True, help= 'Path for the image')
args = vars(ap.parse_args())


image = cv2.imread(args['i'])


# blurred image with Averaging Kernal
# the second argument is the size of the kernal
ave_blur = cv2.blur(image, (5,5)) 


# blurred image with Gaussian Kernal or Weighted Kernal
# the second argument is Kernal Size and third argument is Standard Diviation - 0 means it will std will autamatically calculated 
gau_blur = cv2.GaussianBlur(image, (5,5), 0)


# blurred image with Median Kernal
# the second argument is Kernal Size
med_blur = cv2.medianBlur(image, 5)


# blurred image using Bilateral Kernal
# this technique will preserves the edges in image but slower than other techniques
# second argument is the Kernal Size(diameter of our pixel neighbourhood), third argument is number of colors to be considered,
# fourth is space sigma, larger sigma means pixels far from hotspot also will considered in blurring
bil_blur = cv2.bilateralFilter(image, 5, 21, 21)


horizontally_stacked = np.hstack([image, ave_blur, gau_blur, med_blur, bil_blur])

cv2.imshow('Original', image)
cv2.imshow('Average Blurred', ave_blur)
cv2.imshow('Gaussian Blurred', gau_blur)
cv2.imshow('Median Blurred', med_blur)
cv2.imshow('Bilateral Blurred', bil_blur)
cv2.imshow('All in Horizontally', horizontally_stacked)

cv2.waitKey(0)