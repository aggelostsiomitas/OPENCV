import cv2 as cv 
import numpy as np 


blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#mnake the image green 
blank[:]=0,255,0 #green
cv.imshow('Green',blank)

#add a yellow pixel in the image 
blank[200:300,300:400]=0,255,255
cv.imshow('Yellow',blank)


#draw a rectangle(image , start point , end point , color,thichness)
# cv.rectangle(blank,(0,0),(250,250),(255,255,255),thickness=cv.FILLED)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=cv.FILLED)
cv.imshow('Rectabgle',blank)


#draw a circle(image , center,radius,color,thickness)
cv.circle(blank,(250,250),40,(250,0,0),thickness=cv.FILLED) 
cv.imshow('Circle',blank)


#draw a line(image , start point , edn point ,color) 
cv.line(blank,(0,0),(blank.shape[1],blank.shape[0]),(255,162,164))
cv.imshow('Line',blank)

#write text(image,text,potition,fontface,scale.color,thickness) 
cv.putText(blank,'HELLO',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('Text',blank)

# Keep window open until 'q' is pressed
while True:
    if cv.waitKey(0) & 0xFF == ord('q'):
        break

cv.waitKey(0)
