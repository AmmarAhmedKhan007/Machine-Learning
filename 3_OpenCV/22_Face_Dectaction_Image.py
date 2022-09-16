
import cv2 as cv
import numpy as np

# Create Cascade
face_cascade= cv.CascadeClassifier('Resources\haarcascade_frontalface_default.xml')

img= cv.imread("Resources\detect2.jpg")
# img= cv.resize(img, (600,600))
gray_img= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# print(img.shape)

faces= face_cascade.detectMultiScale(gray_img, 1.1, 4)

# Draw rectangle
for (x, y, w, h) in faces:
    cv.rectangle(img, (x,y),(x+w, y+h),(255,0,0), 2)    

cv.imshow("Image", img)   # Show image
#cv.imwrite("Resources\detect_img.jpg", img)  # Save


cv.waitKey(0)
cv.destroyAllWindows