import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import easyocr

car_img = cv.imread("D:/Training Image Processing/car_plate2.jpg")
car_plate_img =  cv.imread("D:/Training Image Processing/plate_car_num_2.jpg")

#car_img = cv.imread("D:/Training Image Processing/car_plate3.jpg")
#car_plate_img =  cv.imread("D:/Training Image Processing/plate_car_num_3.jpg")


plt.imshow(cv.cvtColor(car_plate_img, cv.COLOR_BGR2RGB))


reader = easyocr.Reader(['en'])
#reader = easyocr.Reader(['fa'])
plate_info = reader.readtext(car_plate_img)

print(plate_info)

plate_text = plate_info[0][1]

print(plate_text)