import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i','-image', required = True, help = 'Enter the path of the image')
args = vars(ap.parse_args())

#read image from the source
image = cv2.imread(args['i'])

# b,g,r = image[0,0]
# print(f'Pixel at (0,0)- Red: {r}, Green: {g}, Blue: {b}')

def get_pixel_and_print(image,u,v):
	"""
		This function will print the pixel values of given coordinates u,v
	"""
	b,g,r = image[u,v]
	print(f'Pixel at ({u},{v})- Red: {r}, Green: {g}, Blue: {b}')


def print_all_pixel_values(image):
	"""
		this function will print the pixel values of a given image
	"""
	[get_pixel_and_print(image,u,v) for u in range(image.shape[0]) for v in range(image.shape[1])]

def set_pixel_value(image, u,v,bgr):
	"""
		this function will get image as an argument and change the desired pixel u,v with the given pixel value and return the image
		note the bgr is a tuple of blue, green, red values, order is important
	"""
	image[u, v] = bgr
	return image 


if __name__ == '__main__':
	# print_all_pixel_values(image)

	print(f'Value of Pixel (0,0): {image[0,0]}\n')
	print('setting the pixel value of (0,0).................................................\n')
	image = set_pixel_value(image, 0, 0, (255,255,255))
	print(f'After setting, value of Pixel (0,0): {image[0,0]}\n')


	#Selecting a Region of Picture and displaying
	corner = image[0:100,0:100]
	cv2.imshow("Corner", corner)
	cv2.waitKey(0)