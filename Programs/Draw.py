import cv2 as cv
import numpy as np
import silence_tensorflow.auto
import tensorflow as tf



blank = np.array(tf.random.normal([500,500,3]))

cv.imshow("Something",blank)


# To color certain portion of the image give blank some range like blank[200:350]
blank[:]=255,0,0  #BGR format
cv.imshow("Blue",blank)



rectangle=cv.rectangle(blank,(0,0),(250,500),(0,255,0),cv.FILLED)
cv.imshow("Rectangle",rectangle)


Circle=cv.circle(blank,(125,125),40,(0,0,255),-1)
cv.imshow("Circle",Circle)


Line=cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),3)
cv.imshow("Line",Line)


Text=cv.putText(blank,"Ashutosh Pandey",(190,300),cv.FONT_HERSHEY_DUPLEX,1.0,(0,0,255),2)
cv.imshow("Name",Text)

cv.waitKey(0)

