import cv2 as cv
import numpy as np

# return image as a matrix of pixels
img = cv.imread("data/photos/cat.jpg")


# display the image
if img is not None:
    cv.imshow("cropped", img[200:400, 200:400])
    b, g, r = cv.split(img)

    # cv.imshow(winname="cat 1", mat=g)
    # cv.imshow(winname="cat 2", mat=r)

    zeros = np.zeros_like(b)
    blue_image = cv.merge([b, zeros, zeros])
    cv.imshow(winname="cat 0", mat=blue_image)

cv.waitKey(0)
cv.destroyAllWindows()

# capture = cv.VideoCapture('data/videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('video', frame)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()
