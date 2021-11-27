# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import numpy as np

image_file = 'C:/Users/NLP Lab/Desktop/lena.jpg'
input_image = cv2.imread(image_file)
grayscale_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", grayscale_image)
cv2.waitKey(0)

Gx = np.array([[1.0, 0.0, -1.0], [2.0, 0.0, -2.0], [1.0, 0.0, -1.0]])
Gy = np.array([[1.0, 2.0, 1.0], [0.0, 0.0, 0.0], [-1.0, -2.0, -1.0]])

imgX = cv2.filter2D(src=grayscale_image, ddepth=-1, kernel=Gx)
imgY = cv2.filter2D(src=grayscale_image, ddepth=-1, kernel=Gy)
cv2.imshow("Sobel X Axis",imgX)
cv2.waitKey(0)
cv2.imshow("Sobel Y Axis",imgY)
cv2.waitKey(0)


final_out = np.sqrt( np.multiply(imgX,imgX) + np.multiply(imgY,imgY) )
final_out = (final_out-final_out.min())/(final_out.max()-final_out.min())*255

threshold = 150
final_out[final_out > threshold] = 255
final_out[final_out <= threshold] = 0

final_out = np.array(final_out,np.uint8)

print(final_out[:2], final_out.dtype, imgX.dtype)

cv2.imshow("Final Output",final_out)
cv2.waitKey(0)
