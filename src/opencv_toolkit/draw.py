import os

import cv2 as cv
import numpy as np

print(os.path.abspath("data/photos/cat.jpg"))
print(np.abs(1))

img = cv.imread("data/photos/cat.jpg")

if img is not None:
    cv.imshow("cat", img)
    # cv.waitKey(0)


blank_img = np.zeros((500, 500, 3), dtype="uint8")

# 1. paint the image a certain color
# blank_img[:] = 0, 255, 0
# blank_img[300:400, 400:500] = 0, 255, 0

# print(blank_img.shape)
# print(blank_img)

# 2. draw a rectangle
# cv.rectangle(blank_img, (0, 0), (250, 250), (0, 255, 0), thickness=2)
cv.rectangle(
    blank_img, (0, 0), (blank_img.shape[1] // 2, blank_img.shape[0] // 2), (0, 255, 0), thickness=-1
)

# 3. draw a circle
cv.circle(blank_img, center=(250, 250), radius=40, color=(0, 0, 255), thickness=3)

# 4. draw a line
cv.line(img=blank_img, pt1=(125, 125), pt2=(325, 325), color=(255, 0, 0), thickness=2)

# 5. write text on img
cv.putText(
    img=blank_img,
    text="Hello, it's me.",
    org=(100, 400),
    fontFace=cv.FONT_HERSHEY_TRIPLEX,
    fontScale=1.0,
    color=(0, 255, 0),
    thickness=2,
)

if blank_img is not None:
    cv.imshow("blank", blank_img)

cv.waitKey(0)
