import cv2 as cv


def resized(frame,scale=1):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)


def resizevideo(capture,scale=1):
    try:
        while True:
            isTrue,frame = capture.read()
            cv.imshow("Resized_Video",resized(frame,scale))
            if cv.waitKey(20) & 0xFF==ord('e'):
                break
        capture.release()
        cv.destroyAllWindows()
    except: 
        AssertionError
        capture.release()
        cv.destroyAllWindows()