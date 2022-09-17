
import cv2 as cv
from cv2 import cvtColor

img= cv.imread("Resources\img.jpg")

gray= cvtColor (img, cv.COLOR_BGR2GRAY)

(thresh, b_w)= cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

# Size
img= cv.resize(img, (800,800))
gray= cv.resize(gray, (800,800))
b_w= cv.resize(b_w, (800,800))

# Display image
cv.imshow("First image", img)
cv.imshow("Gray image", gray)
cv.imshow("Black & White image", b_w)

# Delay
cv.waitKey(0)
cv.destroyAllWindows()