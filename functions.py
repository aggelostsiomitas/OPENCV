import cv2 as cv 

img=cv.imread('Resources/Photos/park.jpg')
cv.imshow('Cat',img)

#convert to grayscale cvtColor(image,color) 
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray image',gray)


#blur  GaussianBlur(image,window size(x,y) for blur x,y must be odd ,sigmaX)
blur=cv.GaussianBlur(img,(11,11),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)


#find edges Cascade(image,threshold1,threshold2,edges,appertureSize) 
canny=cv.Canny(img,125,175)
cv.imshow('Canny',canny)

#find edges in blured image 
canny2=cv.Canny(blur,125,175)
cv.imshow('Canny2',canny2)

#dilating the image (expanding the thichness of the edges)   
# dilate(image,kernel size,iterations)
dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Dilated',dilated)


#eroding  the image (making the edges less thick)
# eroed(image,window kernel (x,y) ,iterations)
eroded=cv.erode(dilated,(3,3),iterations=1,)
cv.imshow('Eroded',eroded)


#resize the image 
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized image',resized)


#croping an image
cropped=img[50:300,50:300]
cv.imshow('Cropped image ',cropped)

cv.waitKey(0)