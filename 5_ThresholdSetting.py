import numpy as np
import cv2 as cv

img = cv.imread('D:/Training Image Processing/BookPage.jpg',cv.IMREAD_COLOR)
cv.imshow('original', img)

#ret,thereshold = cv.threshold(img,10,255,cv.THRESH_BINARY)
imggray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,threshold = cv.threshold(img,12,255,cv.THRESH_BINARY)
cv.imshow('thereshold', threshold)


#OTSU Thereshold
ret2,threshold2 = cv.threshold(imggray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow('thereshold otsu', threshold2)

#adaptive Threshold
threshold3 = cv.adaptiveThreshold(imggray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,115,1)
cv.imshow('thereshold adaptive', threshold3)


cv.waitKey(0)
cv.destroyAllWindows()
