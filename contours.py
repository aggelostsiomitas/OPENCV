import cv2 as cv 
import numpy as np 

img=cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cat',img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank image',blank)


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray cat',gray)

blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blurred gray cat',blur)

#find edges
canny=cv.Canny(img,125,175)
cv.imshow('Canny image',canny)


ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Threshold image',thresh)

#find contours
#findContours(image,mode,method)
contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} found' )


#draw Contours(image,contours,contour index(how many contours i want -1->all of them),color,thickness)
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn at blank image',blank)




cv.waitKey(0)