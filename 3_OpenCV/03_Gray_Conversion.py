
import cv2 as cv
from cv2 import cvtColor

img= cv.imread("Resources\img.jpg")
img= cv.resize(img, (300,300))

# Conversion
gray_img= cv.cvtColor (img, cv.COLOR_BGR2GRAY)

# Display image
cv.imshow("First image", img)
cv.imshow("Gray image", gray_img)

# Delay
cv.waitKey(0)
cv.destroyAllWindows()