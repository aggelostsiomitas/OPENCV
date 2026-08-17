import cv2 as cv 
import numpy as np 

img=cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Laplacian(image,depth,destination,ksize,scale,scale,delta,border tyoe ) 
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Lap',lap)

#Sobel(image,depth,dx,dy)
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobel x',sobelx)
cv.imshow('Sobel y',sobely)
cv.imshow('Combined sobel',combined_sobel)

#Canny 
canny=cv.Canny(gray,150,175)
cv.imshow('Canny',canny)

cv.waitKey(0)