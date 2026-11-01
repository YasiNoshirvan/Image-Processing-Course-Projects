import numpy as np
import cv2 as cv
img = cv.imread('D:/Training Image Processing/blob.jpg',cv.IMREAD_COLOR)
imgray = cv.cvtColor(img,cv.COLOR_BGR2GRAY )

'''
img2 = imgray[100:300,250:500]   #a special part of the image

imgray[100:300,250:500] = 255   # painting white color on the selected area
img[40:150,250:400 ]= 255
'''
'''
blue_blob = img[50:500,70:670]
img[250:700,270:870] = blue_blob  # put the selected area on the image again
'''

#BGR
b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]


img[:,:,2]=0   # remove red color from the picture completely

b,g,r = cv.split(img)
img = cv.merge((b,g,r))




cv.imshow('image',img)

#cv.imshow('image gray',imgray)
#cv.imshow('image crop', img2)

#cv.imshow('blue_blob',blue_blob)

cv.imshow('Blue',b)
cv.imshow('Red',r)
cv.imshow('Green',r)

cv.waitKey(0)
cv.destroyAllWindows()