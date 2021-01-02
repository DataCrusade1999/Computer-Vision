import cv2 as cv

img = cv.imread(r'Photos/Image4.jpg')

#For Image
cv.imshow("Neil",img) 

#For Video
capture = cv.VideoCapture(r'Videos\Video0.webm')
while True:
    isTrue,frame = capture.read()
    cv.imshow("Video",frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()

cv.waitKey(0)