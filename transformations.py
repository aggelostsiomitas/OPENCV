import cv2 as cv 
import numpy as np
 
img=cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park',img)


#translate 
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# x->right 
# -x->left
# y->down 
# -y->up

translated=translate(img,10,10)
cv.imshow('Translated image',translated)

#rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)

    #getRotationMatrix2D(rotation point , angle ,scale)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,45)
cv.imshow('Rotated image',rotated)

#resizing
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resized iomager',resized)


#flip image
flip=cv.flip(img,0)
cv.imshow('Flipped image',flip)



cv.waitKey(0)