import cv2 as cv

def Grayscale(capture):
    while True:
        isTrue,frame = capture.read()
        frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow("Video",frame)

        if cv.waitKey(20) & 0xFF==ord('e'):
            break
    capture.release()
cv.destroyAllWindows()