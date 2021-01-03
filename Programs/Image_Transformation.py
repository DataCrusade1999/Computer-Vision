import cv2 as cv
from Modules.translation import translate


img = cv.imread(r'C:\Users\ashut\Computer-Vision\Photos\Image4.jpg')

cv.imshow("Image",img)

cv.waitKey(0)
cv.destroyAllWindows()


translate(img,100,100)
cv.waitKey(0)