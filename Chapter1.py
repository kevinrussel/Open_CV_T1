import cv2
## this is for images.
# img = cv2.imread("Images/Cat1.jpg")
# cv2.imshow("Output",img)
# cv2.waitKey(0)
 
 ## This is for videos.
# cap = cv2.VideoCapture("Images/World.mp4")
# Since an image is just a Frames 1 after another we can do a while loop
# while True:
#     # The first variable is just a boolean to see if we got it or not
#     success, img = cap.read()
#     cv2.imshow("Output", img)
#     # this is waiting for the dealy. Looks for the keypress q to run out of the loop.
#     if cv2.waitKey(1) & 0xFF ==ord("q"):
#         break

## This is for the webcam

# webCam = cv2.VideoCapture(0)

# webCam.set(3,640) ## This is setting the width (3) to 640
# webCam.set(4,480) ## This is setting the height (4) to 480
#clear webCam.set(10,5) # this is changing the brightness (10) to 100.
# while True:
#     sucess, img = webCam.read()
#     cv2.imshow("Output",img)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break