import cv2 as cv 

img=cv.imread('Resources/Photos/cat.jpg')

cv.imshow('Cat',img)

#for images and videos
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale) #columns
    height=int(frame.shape[0]*scale) #rows
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)



#for live videos
def changeRes(capture,width,height):
    capture.set(3,width)
    capture.set(3,height)


#resize image 
resized_image=rescaleFrame(img)
cv.imshow('Image',resized_image)
capture=cv.VideoCapture('Resources/Videos/dog.mp4')

#change resolution
changeRes(capture, 640, 480)



while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleFrame(frame,scale=0.2)
    #show the videos
    cv.imshow('Video',frame)
    cv.imshow('Rescaled Video',frame_resized)

    #break condition q letter
    if cv.waitKey(20)& 0xFF==ord('q'):
        break 

#destroy video when finished    
capture.release()
cv.destroyAllWindows()
cv.waitKey(0) 