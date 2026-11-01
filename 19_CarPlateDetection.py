import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import imutils

car_img = cv.imread("D:/Training Image Processing/car_plate3.jpg")
car_img_gray = cv.cvtColor(car_img, cv.COLOR_BGR2GRAY)

blateral_filtered = cv.bilateralFilter(car_img_gray, 11, 15, 15)
edges = cv.Canny(blateral_filtered, 30, 200)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv.cvtColor(car_img, cv.COLOR_BGR2RGB))
plt.title('Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Canny Edges')
plt.axis('off')


contours = cv.findContours(edges.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours_refind = imutils.grab_contours(contours)
contours_sorted = sorted(contours_refind, key=cv.contourArea, reverse=True)[:30]

plate_location = None

for contour in contours_sorted:
    perimeter = cv.arcLength(contour, True)
    contour_approx = cv.approxPolyDP(contour, 0.02 * perimeter, True)

    if len(contour_approx) == 4:
        x, y, w, h = cv.boundingRect(contour_approx)
        aspect_ratio = w / h

        if 2.5 < aspect_ratio < 6:
            plate_location = contour_approx
            break


if plate_location is None:
    print("License plate not detected!")

else:
    plate_mask0 = np.zeros(car_img_gray.shape, np.uint8)
    plate_mask = cv.drawContours(plate_mask0, [plate_location], 0, 255, -1)
    plate_img = cv.bitwise_and(car_img, car_img, mask=plate_mask)

    plt.figure(figsize=(10, 5))
    plt.imshow(cv.cvtColor(plate_img, cv.COLOR_BGR2RGB))
    plt.title('Detected License Plate')
    plt.axis('off')

    # Save detected plate image
    cv.imwrite("D:/Training Image Processing/plate_car_3.jpg", plate_img)

    # Crop license plate (Professor's code)
    (x, y) = np.where(plate_mask == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))

    cropped_image = car_img_gray[x1:x2+1, y1:y2+1]

    plt.figure(figsize=(10, 4))
    plt.imshow(cropped_image, cmap='gray')
    plt.title('Cropped License Plate')
    plt.axis('off')

    # Save cropped plate
    cv.imwrite("D:/Training Image Processing/plate_car_num_3.jpg", cropped_image)

plt.show()