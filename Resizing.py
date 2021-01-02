import cv2 as cv
from  Modules.Resize import resized as rs


#For Video
capture = cv.VideoCapture(r'Videos\Video0.webm')
while True:
    isTrue,frame = capture.read()
    cv.imshow("Video",frame)
    resized_Video=rs(frame)
    cv.imshow("Resized_Video",resized_Video)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()

#For Image
img=cv.imread(r'Photos\Image3.jpg')
cv.imshow("Resized_Image",rs(img))
cv.waitKey(0)



