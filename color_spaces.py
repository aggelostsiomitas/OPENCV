import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 


img=cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park',img)


#BGR to Gray scale 
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray image',gray)

#BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)


#BGR to L*a*b
Lab=cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('HSV',Lab)


rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)


plt.imshow(rgb)
plt.show()
cv.waitKey(0)