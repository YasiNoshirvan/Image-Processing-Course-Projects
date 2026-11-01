import numpy as np
import cv2 as cv

img1 = cv.imread('D:/Training Image Processing/vsls1.jpg',cv.IMREAD_COLOR)
img2 = cv.imread('D:/Training Image Processing/vsls3.jpg',cv.IMREAD_COLOR)

#cv.imshow('image 1',img1)
#cv.imshow('image 2',img2)

# Resize image 2 to match image 1
height, width = img1.shape[:2]
img2 = cv.resize(img2, (width, height))

#method 1
#added = img1 + img2
#cv.imshow('Added', added)

#method2
#added = cv.add(img1,img2)
#cv.imshow('Added', added)


#method3
#added = cv.addWeighted(img1,0.8,img2,0.2, 0)
#cv.imshow('Added', added)

#method4
img1gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
ret,maskimg = cv.threshold(img1gray,40,255,cv.THRESH_BINARY)

mask_inv = cv.bitwise_not(maskimg)

img2_m = cv.bitwise_and(img2,img2,mask=mask_inv)
img1_m = cv.bitwise_and(img1,img1,mask=maskimg)
imgadded = cv.add(img2_m,img1_m)

cv.imshow('mask2', img2_m)
cv.imshow('mask1', img1_m)
cv.imshow('image added', imgadded)



cv.waitKey(0)
cv.destroyAllWindows()