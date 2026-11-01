import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

#image = cv.imread('D:/Training Image Processing/shapes.jpg')
#image_gr = cv.imread('D:/Training Image Processing/shapes.jpg', 0)


#image = cv.imread('D:/Training Image Processing/PinWheel.jpg')
#image_gr = cv.imread('D:/Training Image Processing/pinWheel.jpg', 0)

image = cv.imread('D:/Training Image Processing/box.jpg')
image_gr = cv.imread('D:/Training Image Processing/box.jpg', 0)


corners = cv.cornerHarris(image_gr, 2, 5, 0.04)
corner_dilated = cv.dilate(corners, None)

image[corner_dilated>0.01*corner_dilated.max()] = [255,0,0]

plt.imshow(image)
plt.show()


