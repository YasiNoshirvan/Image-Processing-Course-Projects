import cv2 as cv
import numpy as np
from cvzone.HandTrackingModule import HandDetector

cap = cv.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=2)

while(True):
    rec, frame = cap.read()

    if not rec:
        break

    hand, img = detector.findHands(frame, draw=True)

    if hand:
        hand1 = hand[0]
        lmlist1 = hand1["lmList"]

        length, info, img = detector.findDistance(lmlist1[4][:-1], lmlist1[8][:-1], img)

        print(f"length: {str(length)}")

    cv.imshow('frame', img)

    keyexit = cv.waitKey(5) & 0xFF
    if keyexit == 27:
        break

cap.release()
cv.destroyAllWindows()