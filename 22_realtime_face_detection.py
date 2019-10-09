import face_recognition
import cv2
from PIL import Image, ImageDraw



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

	video_capture = cv2.VideoCapture(0)
	# face_locations = []
	# face_encodings = []
	face_names = []

	process_this_frame = True


	while True:
		# grapping a frame
		ret, frame = video_capture.read()

		# resizing frame for faster recognition
		small_frame = cv2.resize(frame, (0,0), fx = 0.25, fy = 0.25)

		# converting from BGR color format to RGB format
		rgb_frame = small_frame[:,:,::-1]


		if process_this_frame:
			# find all faces in frame and their encodings
			face_locations = face_recognition.face_locations(rgb_frame)
			face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

			face_names = []

			for face_encoding in face_encodings:

				matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
				name = 'Unknown'

				if True in matches:
					first_match_index = matches.index(True)
					name = known_face_names[first_match_index]

				face_names.append(name)

		process_this_frame = not process_this_frame

		# iterate over all faces found in image
		for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
			
			top *= 4
			right *= 4
			bottom *= 4
			left *= 4

			# draw box around face
			cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)

			# draw label with name
			cv2.rectangle(frame, (left, bottom-35), (right, bottom), (0,255,0), cv2.FILLED)
			font = cv2.FONT_HERSHEY_DUPLEX
			cv2.putText(frame, name, (left+6, bottom-6), font, 0.5, (255,255,255), 1)

		cv2.imshow('Video', frame)

		if cv2.waitKey(1) & 0xFF == ord ('q'):
			break


	video_capture.release()
	cv2.destroyAllWindows()






