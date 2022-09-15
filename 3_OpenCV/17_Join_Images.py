
import cv2 as cv
import numpy as np

img= cv.imread("Resources\img.jpg")
img= cv.resize(img, (600,600))

# Staking Image
# 1_Horizonta Stack:
hor_img= np.hstack((img, img))
# 2_Vertical Stack:
ver_img= np.vstack((img, img))


# Show Image
# cv.imshow("First image", img)
cv.imshow("Horizontal_image", hor_img)
cv.imshow("Vertical_image", ver_img)


# Delay
cv.waitKey(0)
cv.destroyAllWindows()