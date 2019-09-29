import argparse
import cv2
import matplotlib.pyplot as plt

#fetch
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required =True, help="Enter path to the image: ")
args = vars(ap.parse_args())

#load image from disk image will loaded into numpy array
image = cv2.imread(args['image'])
print("height:{} pixels".format(image.shape[0]))
print("width:{} pixels".format(image.shape[1]))
print("channels:{}".format(image.shape[2]))

#show the image and save in another format

#display image
cv2.imshow("Image", image)
#wait key 0 mean indifinite wait, 1000 means wait for 1sec
cv2.waitKey(0)
#write to jpg format
cv2.imwrite('cat.jpg',image)