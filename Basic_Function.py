import cv2 as cv
from Modules.Resize import resized as rs
from Modules.Gray import Grayscale 

#BGR Image in Grayscale
img = cv.imread(r"Photos\Image0.jpg")
img = rs(img,0.40)
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale",img)
cv.waitKey(0)
cv.destroyAllWindows()


#Blur
img = cv.imread(r"Photos\Image4.jpg")
img = rs(img,0.57)
cv.imshow("Not_Blurred",img)
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
canny = cv.Canny(blur,125,175)
cv.imshow("Blur_Edge",canny)
cv.waitKey(0)
cv.destroyAllWindows()



#Video in Grayscale
capture = cv.VideoCapture(r'Videos\Video0.webm')

Grayscale(capture)



#Edge Cascade
img = cv.imread(r"Photos\Image4.jpg")
img = rs(img,0.57)
canny = cv.Canny(img,125,175)
cv.imshow("Edge",canny)
cv.waitKey(0)
cv.destroyAllWindows()

#Dilating Edge
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow("Dilated",dilated)
cv.waitKey(0)
cv.destroyAllWindows()

#Eroding
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow("Eroded",eroded)
cv.waitKey(0)
cv.destroyAllWindows()


#Resizing
img = cv.imread(r"Photos\Image4.jpg")
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",resized)
cv.waitKey(0)
cv.destroyAllWindows()