import cv2 as cv
from  Modules.Resize import resized as rs
from  Modules.Resize import resizevideo as rsv

#For Video
capture = cv.VideoCapture(r'Videos\Video0.webm')
rsv(capture,0.20)

#For Image
img=cv.imread(r'Photos\Image3.jpg')
cv.imshow("Resized_Image",rs(img))
cv.waitKey(0)
