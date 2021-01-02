import cv2 as cv
from Modules.Resize import resized as rs


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
cv.imshow("Blur",blur)
cv.waitKey(0)
cv.destroyAllWindows()



#Video in Grayscale
capture = cv.VideoCapture(r'Videos\Video0.webm')
while True:
    isTrue,frame = capture.read()
    frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow("Video",frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()


#Edge Cascade
img = cv.imread(r"Photos\Image4.jpg")
img = rs(img,0.57)
canny = cv.Canny(img,125,175)
cv.imshow("Edge",canny)
cv.waitKey(0)
cv.destroyAllWindows()