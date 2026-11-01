import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


#original_img = cv.imread('D:/Training Image Processing/Neuron.jpg',0)
original_img = cv.imread('D:/Training Image Processing/cells_threshold.jpg',0)

_,mask = cv.threshold(original_img,25,255,cv.THRESH_BINARY)

# Erosion
#kernel = np.ones((3,3), np.uint8)
#eroded_img = cv.erode(mask, kernel, iterations=1)

# Dilation
#kernel = np.ones((3,3), np.uint8)
#dilated_img = cv.dilate(mask, kernel, iterations=1)
#kernel = np.ones((3,3), np.uint8)
#eroded_img = cv.erode(mask, kernel, iterations=1)

# Closing
#kernel1 = np.ones((3,3), np.uint8)
#closed_img1 = cv.morphologyEx(mask, cv.MORPH_CLOSE,kernel1)
#kernel2 = np.ones((5,5), np.uint8)
#closed_img2 = cv.morphologyEx(mask, cv.MORPH_CLOSE,kernel2)

# Opening
#kernel1 = np.ones((9,9), np.uint8)
#opened_img1 = cv.morphologyEx(mask,cv.MORPH_OPEN,kernel1)
#kernel2 = np.ones((25,25), np.uint8)
#opened_img2 = cv.morphologyEx(mask,cv.MORPH_OPEN,kernel2)

# Gradient
kernel1 = np.ones((5,5), np.uint8)
gradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel1)

kernel2 = np.ones((5,5), np.uint8)
dilated_img = cv.dilate(mask, kernel2, iterations=1)
subtract_img = dilated_img -mask


fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(10, 20))
cmap_val = 'gray'
ax1.axis("off")
ax1.title.set_text('')
ax2.axis("off")
ax2.title.set_text('')
ax3.axis("off")
ax3.title.set_text('')
#ax1.imshow(original_img, cmap=cmap_val)
ax1.imshow(mask, cmap=cmap_val)
#ax2.imshow(dilated_img, cmap=cmap_val)
#ax3.imshow(eroded_img, cmap=cmap_val)
#ax2.imshow(closed_img1, cmap=cmap_val)
#ax3.imshow(closed_img2, cmap=cmap_val)
#ax2.imshow(opened_img1, cmap=cmap_val)
#ax3.imshow(opened_img2, cmap=cmap_val)
ax2.imshow(gradient, cmap=cmap_val)
ax3.imshow(subtract_img, cmap=cmap_val)
plt.show()