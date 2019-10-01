import face_recognition
import numpy as np
import argparse
import cv2
from PIL import Image, ImageDraw


ap = argparse.ArgumentParser()
ap.add_argument('-i', required = True, help = 'Path to Image')
args = vars(ap.parse_args())

image = cv2.imread(args['i'])

known_face_encodings = []

known_face_names = []

def load_and_encode(path, name):
	"""
	this function will get an image path and name as input:  load, encode and then put the encodings into the appropriate lists
	pass front facing clear images with only the respective person
	"""
	person = face_recognition.load_image_file(path)
	person_encoded = face_recognition.face_encodings(person)[0]

	known_face_encodings.append(person_encoded)
	known_face_names.append(name)



if __name__ == '__main__':
	load_and_encode('/home/mr/Desktop/face_rec/mathan.jpg', "Mathanraj Sharma")
	load_and_encode('/home/mr/Desktop/face_rec/vithu.jpg', "Vithursha Sivakumar ")
	load_and_encode('/home/mr/Desktop/face_rec/shan.jpg', "Joseph Shan Fravin")
	load_and_encode('/home/mr/Desktop/face_rec/ajanthy.jpg', "Ajanthy Jayarajan")

	face_locations = face_recognition.face_locations(image)
	face_encodings = face_recognition.face_encodings(image, face_locations)

	# convert image to PIL format so we can draw on top of the image
	pil_image = Image.fromarray(image)

	# creating a draw object to draw on image, like a pencil
	draw = ImageDraw.Draw(pil_image)

	# iterate over all faces found in image
	for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
		#this will return a boolean list by comparing face_encoding with the known_face_encodings
		matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
		name = 'Unknown'

		# selecting first match from matches
		if True in matches:
			first_match_index = matches.index(True)
			name = known_face_names[first_match_index]

		# draw a rectangle around the face from left top to right bottom
		draw.rectangle(((left, top), (right, bottom)), outline = (0,255,0))

		# naming the face
		text_width, text_height = draw.textsize(name)
		draw.rectangle(((left, bottom - text_height - 10), (right, bottom)),fill = (0,0,255), outline = (0,0,255))
		draw.text((left + 6, bottom - text_height - 5), name, fill = (255,255,255))


	del draw

	pil_image.show()



