import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
'''
image = cv.imread('D:/Training Image Processing/jumbo.jpg')

# SIFT
feat_sift = cv.SIFT_create()

# SURF
#feat_surf = cv.xfeatures2d.SURF_create()

# ORB
feat_orb = cv.ORB_create(nfeatures = 100)


sift_keypoints, description1 = feat_sift.detectAndCompute(image, None)
image_sift = cv.drawKeypoints(image, sift_keypoints, None)

plt.subplot(121)
plt.imshow(cv.cvtColor(image_sift, cv.COLOR_BGR2RGB))
plt.title('SIFT')


#surf_keypoints, description2 = feat_surf.detectAndCompute(image, None)
#image_surf = cv.drawKeypoints(image, surf_keypoints, None)

#plt.subplot(122)
#plt.imshow(cv.cvtColor(image_surf, cv.COLOR_BGR2RGB))
#plt.title('Surf')


orb_keypoints, description3 = feat_orb.detectAndCompute(image, None)
image_orb = cv.drawKeypoints(image, orb_keypoints, None)

plt.subplot(122)
plt.imshow(cv.cvtColor(image_orb, cv.COLOR_BGR2RGB))
plt.title('ORB')

plt.show()

'''

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

image1 = cv.imread('D:/Training Image Processing/book2.jpg')
image2 = cv.imread('D:/Training Image Processing/book1.jpg')

# ORB
feat_orb = cv.ORB_create(nfeatures = 100)

orb_keypoints1, description1 = feat_orb.detectAndCompute(image1, None)
orb_keypoints2, description2 = feat_orb.detectAndCompute(image2, None)

bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches = bf.match(description1,description2)
matches = sorted(matches, key=lambda x:x.distance)
image_matches = cv.drawMatches(image1,orb_keypoints1, image2, orb_keypoints2, matches[:100], None, flags=20)

plt.imshow(image_matches)
plt.show()