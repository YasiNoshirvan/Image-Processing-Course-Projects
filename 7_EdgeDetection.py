import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('D:/Training Image Processing/road_in_norway_.jpg', 0)
image_noise_remove = cv.GaussianBlur(image, (3, 3), 0)

# Laplacian
laplacian = cv.Laplacian(image_noise_remove, cv.CV_64F)

# Sobel X
sobelx = cv.Sobel(image_noise_remove, cv.CV_64F, 1, 0, ksize=5)

# Sobel Y
sobely = cv.Sobel(image_noise_remove, cv.CV_64F, 0, 1, ksize=5)

# Canny Edge Detection
canny = cv.Canny(image_noise_remove, 100, 200)


plt.figure(figsize=(12, 8))

# Top Left - Original
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original')
plt.xticks([])
plt.yticks([])

# Top Right - Canny
plt.subplot(2, 2, 2)
plt.imshow(canny, cmap='gray')
plt.title('Canny')
plt.xticks([])
plt.yticks([])

# Bottom Left - Sobel X
plt.subplot(2, 2, 3)
plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X')
plt.xticks([])
plt.yticks([])

# Bottom Right - Sobel Y
plt.subplot(2, 2, 4)
plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y')
plt.xticks([])
plt.yticks([])

plt.tight_layout()
plt.show()