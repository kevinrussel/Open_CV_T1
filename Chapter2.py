import cv2
import numpy as np

# we are making a matrix
kernal = np.ones((5,5), np.uint8)


img = cv2.imread("Images/Cat1.jpg")

# Converting to grey scale

imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey,(7,7),0)

## this is an edge detector
imgCanny = cv2.Canny(img,100,200)


imgCanny = cv2.resize(imgCanny, None, fx=0.5, fy=0.5)

# This is for making the edge detection better. We can make the edges thicker.
# the iterations is how much thickness we actually need.
imgDialation = cv2.dilate(imgCanny,kernal,iterations=1)


## this is to make the edges thinner( by erosion)
imgEroded = cv2.erode(imgDialation,kernal,iterations=1)

# cv2.imshow("Output",imgGrey)
# cv2.imshow("Blur Image", imgBlur)
cv2.imshow("canny",imgCanny)
cv2.imshow("dialation",imgDialation)
cv2.imshow("errosion",imgEroded)
cv2.waitKey(0)