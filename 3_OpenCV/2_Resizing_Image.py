
import cv2 as cv

img= cv.imread("Resources\img.jpg")
img= cv.resize(img, (800,800))

# Show Image
cv.imshow("First image", img)

# Delay
cv.waitKey(0)
cv.destroyAllWindows()