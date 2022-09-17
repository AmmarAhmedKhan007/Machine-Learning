
import cv2 as cv
from cv2 import cvtColor

img= cv.imread("Resources\img.jpg")

gray= cvtColor (img, cv.COLOR_BGR2GRAY)
(thresh, b_w)= cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

cv.imwrite("Resources\Gray_img.jpg", gray)
cv.imwrite("Resources\Black_&_White.jpg", b_w)