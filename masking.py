import cv2 as cv 
import numpy as np 


img=cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)
blank2=blank.copy()

mask=cv.circle(blank.copy(),(blank.shape[1]//2,blank.shape[0]//2),100,255,-1)
cv.imshow('Mask',mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked',masked)


mask2=cv.rectangle(blank2,(blank2.shape[1]//2,blank2.shape[0]//2),(blank2.shape[1]//2+100,
blank2.shape[0]//2+100),255,-1)

masked2=cv.bitwise_and(img,img,mask=mask2)
cv.imshow('masked2',masked2)

cv.waitKey(0)