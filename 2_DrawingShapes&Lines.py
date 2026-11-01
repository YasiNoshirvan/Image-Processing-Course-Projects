import numpy as np
import cv2 as cv
img = cv.imread('D:/Training Image Processing/cityscape.jpg',cv.IMREAD_COLOR)
'''
cv.line(img, (5,5), (200,150), (200,200,0), 10)
cv.rectangle(img,(5,5),(200,150), (255,255,255),8)
cv.circle(img,(200,150),50,(0,255,255),10)

points= np.array([[30,50],[300,200], [100,70],[40,100]],np.int32)
cv.polylines(img,[points],True, (255,0,0),5)  #customized shapes
'''

font = cv.FONT_HERSHEY_DUPLEX
cv.putText(img,'Hello world!',(30,60), font, 2,(255,255,255),4,cv.LINE_AA)

cv.imshow('city', img)
cv.waitKey(0)
cv.destroyAllWindows()
