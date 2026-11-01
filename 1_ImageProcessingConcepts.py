
import numpy as np
import cv2 as cv    # openCV library

## with imread
img = cv.imread('D:/Training Image Processing/cityscape.jpg',cv.IMREAD_GRAYSCALE)  # load image in Black&White  # or 0
                                                            #cv.IMREAD_COLOR       # load image in Black&White   # or 1
                                                    #cv.IMREAD_UNCHANGED   # load image as itself    # or -1
imgCol = cv.imread('D:/Training Image Processing/cityscape.jpg',cv.IMREAD_COLOR)

#cv.imshow('IMAGE display', img)   #IMAGE display ~ title of show windom
cv.imshow('IMAGE Colorful display', imgCol)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('D:/Training Image Processing/cityscape_gray.jpg',img)  #save the jpg file


#RGB (    34  ,    45     ,    56   )
#    (red canal, green canal, blue canal)
# in opencv  --> coloring system --> BGR --> (blue canal, green canal, red canal)



## with matplotlib
from matplotlib import pyplot as plt
#plt.imshow(img, cmap='grey',interpolation='bicubic')
plt.imshow(imgCol,interpolation='bicubic')
#plt.plot([50,100],[100,200],'c',linewidth=5)  #put a line on the picture
plt.show()