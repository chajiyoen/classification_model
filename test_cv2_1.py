import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot  as plt
timg = cv.imread(r"d:\test\a2.jpg",cv.IMREAD_COLOR)
timg = cv2.resize(timg, (256, 256))
gray = cv2.cvtColor(timg, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
bg_removed = cv2.bitwise_and(timg, timg, mask=mask)

cv2.imshow("Original Image", timg)
cv2.imshow("Foreground Mask", mask)
cv2.imshow("Background Removed", bg_removed)

cv.waitKey(0)
cv.destroyAllWindows()