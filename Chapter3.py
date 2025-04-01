import cv2

img = cv2.imread("Images/Cat1.jpg")
# To find the size of the img
# 2397 ( height), 1795 (width), 3 ( channels) (bgr)
print(img.shape)

# to resize
imgResize = cv2.resize(img,(300,300))

# To crop an img starting point and ending point ( HEIGHT COMES FIRST)
imgCropped = img[200:1000, 0:1000]

cv2.imshow("Img",img)
cv2.imshow("Img rezie", imgResize)
cv2.imshow("Cropped",imgCropped)
cv2.waitKey(0)