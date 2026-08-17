import cv2 as cv 
import matplotlib.pyplot as plt 


img=cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#GRAYSCALE HISTOGRAM 
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.plot(gray_hist)
plt.title('Grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('number of pixels')
plt.xlim([0,256])

plt.show()


cv.waitKey(0)