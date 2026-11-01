import numpy as np
import cv2 as cv

def rescale_frame(frame, percent=20):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

cap = cv.VideoCapture("D:/Training Image Processing/videos/street_camera.mp4")

while(True):
    rec1, frame1 = cap.read()
    rec2, frame2 = cap.read()

    if not rec1 or not rec2:
        break

    resized_frame1 = rescale_frame(frame1, 15)
    resized_frame2 = rescale_frame(frame2, 15)

    frame_diff = cv.absdiff(resized_frame1, resized_frame2)

    # Convert BGR to Grayscale
    frame_diff_gr = cv.cvtColor(frame_diff, cv.COLOR_BGR2GRAY)

    blurred_frame = cv.GaussianBlur(frame_diff_gr, (3,3), 1)

    _, mask = cv.threshold(blurred_frame, 10, 255, cv.THRESH_BINARY)

    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv.contourArea(contour) > 1000:
            (x, y, w, h) = cv.boundingRect(contour)
            cv.rectangle(resized_frame1, (x + w - 100, y + h - 100), (x + w, y + h), (0, 0, 225), 2)

    cv.imshow('frame', resized_frame1)
    cv.imshow('frame_diff', frame_diff)
    cv.imshow('mask', mask)

    cv.moveWindow('frame', 20, 50)
    cv.moveWindow('frame_diff', resized_frame1.shape[1] + 50, 50)

    keyexit = cv.waitKey(5) & 0xFF
    if keyexit == 27:
        break

cap.release()
cv.destroyAllWindows()