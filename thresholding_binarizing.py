import cv2 as cv 

img=cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#threshold(image,threshold,max value,type)
threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple threshold',thresh)

threshold,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple threshold inverse',thresh_inv)


#adaptive threshold 
#adaptiveThreshold(image,max value,adaptive method,threshhold type,blocksize,C value) 
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive threshold',adaptive_thresh)


cv.waitKey(0)