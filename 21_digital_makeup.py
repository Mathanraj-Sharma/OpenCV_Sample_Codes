import face_recognition
from PIL import Image, ImageDraw



image = face_recognition.load_image_file('/home/mr/Desktop/face_rec/thushangi.jpg')

#  getting all facial landmarks in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

for face_landmarks in face_landmarks_list:
	pil_image = Image.fromarray(image)
	d = ImageDraw.Draw(pil_image, 'RGBA')


	# making eyebrow darker
	d.polygon(face_landmarks['left_eyebrow'], fill = (68, 54, 39, 255))
	d.polygon(face_landmarks['right_eyebrow'], fill = (68, 54, 39, 255))
	d.line(face_landmarks['left_eyebrow'], fill = (68, 54, 39, 255), width = 5)
	d.line(face_landmarks['left_eyebrow'], fill = (68, 54, 39, 255), width = 5)


	# Adding lipstick
	d.polygon(face_landmarks['top_lip'], fill = (255,0,0,128))
	d.polygon(face_landmarks['bottom_lip'], fill = (255,0,0,128))
	d.line(face_landmarks['top_lip'], fill = (255,0,0,64), width = 8)
	d.line(face_landmarks['bottom_lip'], fill = (255,0,0,64), width = 8)

	# adding mascara 
	d.line(face_landmarks['left_eye']+ [face_landmarks['left_eye'][0]], fill = (0,0,0,125),  width = 6)
	d.line(face_landmarks['right_eye']+ [face_landmarks['right_eye'][0]], fill = (0,0,0,125),  width = 6)

	pil_image.show()