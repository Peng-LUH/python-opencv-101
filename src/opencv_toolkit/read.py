import cv2 as cv

# return image as a matrix of pixels
img = cv.imread("data/photos/cat_large.jpg")

# display the image
if img is not None:
	cv.imshow(winname="cat", mat=img)
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