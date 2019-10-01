from PIL import Image
import face_recognition
import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument('-i', required = True, help = 'Path to image')
args = vars(ap.parse_args())


image = cv2.imread(args['i'])


face_locations = face_recognition.face_locations(image)
print(f'Number of faces in Image: {len(face_locations)}')

for face_location in face_locations:
	top, right, bottom, left = face_location

	face_image = image[top:bottom, left:right]
	pil_image = Image.fromarray(face_image)
	pil_image.show()