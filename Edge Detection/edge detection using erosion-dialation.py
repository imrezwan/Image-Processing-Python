# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 11:42:19 2021

@author: NLP Lab
"""
import cv2
import numpy as np
 
# Reading the input image
img = cv2.imread('C:/Users/NLP Lab/Desktop/Picture1.png', 0)
 
kernel = np.ones((7,7), np.uint8)

img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

ero_edge  = img - img_erosion
dia_edge = img_dilation - img

cv2.imshow('Input', img)
cv2.imshow('Erosion Edge', ero_edge)
cv2.imshow('Dilation Edge', dia_edge)
 
cv2.waitKey(0)
