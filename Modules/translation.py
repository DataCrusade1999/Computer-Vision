import cv2 as cv
import numpy as np

def translate(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0])
    mat = cv.warpAffine(img,transmat,dimension)
    return cv.imshow("Translated Image",mat)