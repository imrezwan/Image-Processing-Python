# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 01:28:10 2020

@author: Pranto
"""

import cv2 

img = cv2.imread('lena.png', 0) 
cv2.imshow('input image', img)

 
r1 = int(input('Value of r1: '))
s1 = int(input('Value of s1: '))
r2 = int(input('Value of r2: '))
s2 = int(input('Value of s2: '))
  
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        x = img.item(i,j)
        if (0 <= x and x <= r1): 
            x = (s1 / r1)*x 
        elif (r1 < x and x <= r2): 
            x = ((s2 - s1)/(r2 - r1)) * (x - r1) + s1 
        else: 
            x = ((255 - s2)/(255 - r2)) * (x - r2) + s2 
        img.itemset((i,j), x)   
  
cv2.imshow('contrast stretch', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()