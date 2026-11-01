import numpy as np
import cv2 as cv  # openCV library
import matplotlib.pyplot as plt

cap = cv.VideoCapture(0)

while(True):
    rec, frame = cap.read()
    frame_hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    #lower_red = np.array([0,50,50])
    #upper_red = np.array([6,255,255])
    #mask_red = cv.inRange(frame_hsv,lower_red,upper_red)

    lower_blue = np.array([100,50,50])
    upper_blue = np.array([116,255,255])
    mask_blue = cv.inRange(frame_hsv,lower_blue,upper_blue)

    frame_masked = cv.bitwise_and(frame,frame,mask=mask_blue)

    cv.imshow('frame',frame)
  # cv.imshow('mask_blue',mask_red)
    cv.imshow('mask_blue',mask_blue)
    cv.imshow('frame_masked', frame_masked)
    keyexit=cv.waitKey(5) & 0xFF
    if keyexit == 27:
        break

cv.destroyAllWindow()
cap.release()