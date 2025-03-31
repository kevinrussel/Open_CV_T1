import cv2


img = cv2.imread("Images/Cat1.jpg")

# Converting to grey scale

imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey,(7,7),0)



cv2.imshow("Output",imgGrey)
cv2.imshow("Blur Image", imgBlur)
cv2.waitKey(0)