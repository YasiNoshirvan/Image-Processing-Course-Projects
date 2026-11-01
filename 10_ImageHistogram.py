import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

#image = cv.imread('D:/Training Image Processing/xray1.jpg', 0)
#histogram = cv.calcHist([image],[0],None,[256],[0,256])

#image = cv.imread('D:/Training Image Processing/seasons.jpg')

'''
image = cv.imread('D:/Training Image Processing/seasons.jpg')
w,h,c = image.shape
mask = np.zeros(image.shape[0:2],np.uint8)
mask[0:int(w/2),0:int(h/2)] = 255

colors = ['b', 'g', 'r']
for i, col in enumerate(colors):
    histogram = cv.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram, color=col)

#plt.subplot(121) , plt.imshow(image,'gray')
#plt.subplot(122) , plt.plot(histogram)
'''


image = cv.imread('D:/Training Image Processing/statue.jpg',0)
image_hist = cv.calcHist([image], [0], None, [256], [0, 256])
equalized_histogram = cv.equalizeHist(image)
img_equal_hist = cv.calcHist([equalized_histogram],[0],None, [256], [0,256])

clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(image)
cl_equal_hist = cv.calcHist([equalized_histogram],[0],None, [256], [0,256])


plt.subplot(321), plt.imshow(image, 'gray')
plt.subplot(322), plt.plot(image_hist, )
plt.subplot(323), plt.imshow(equalized_histogram, 'gray')
plt.subplot(324), plt.plot(img_equal_hist,)
plt.subplot(325), plt.imshow(equalized_histogram, 'gray')
plt.subplot(326), plt.plot(img_equal_hist, )

#plt.imshow(equalized_histogram,'gray')
plt.show()