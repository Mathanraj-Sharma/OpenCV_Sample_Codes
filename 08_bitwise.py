import cv2
import numpy as np


#lets create two images rectangle and a circle


canvas1 = np.zeros((300,300), dtype = 'uint8')
cv2.rectangle(canvas1, (25,25), (275,275), 255, -1)
cv2.imshow('Canvas1', canvas1)
cv2.waitKey(0)

canvas2 = np.zeros((300,300), dtype = 'uint8')
cv2.circle(canvas2, (150,150), 150, 255, -1)
cv2.imshow('Canvas2', canvas2)
cv2.waitKey(0)

#lets do bitwiese and, or, xor and not

bitwiseAnd = cv2.bitwise_and(canvas1, canvas2)
cv2.imshow('AND', bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(canvas1, canvas2)
cv2.imshow('OR', bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(canvas1, canvas2)
cv2.imshow('XOR', bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(canvas1)
cv2.imshow('NOT', bitwiseNot)
cv2.waitKey(0)