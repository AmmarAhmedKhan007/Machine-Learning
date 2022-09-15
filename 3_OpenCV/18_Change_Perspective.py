
import cv2 as cv
import numpy as np

img= cv.imread("Resources\wrap.png")
img= cv.resize(img, (800,900))

print(img.shape)
# Define Points
point1= np.float32([[233, 196],[82, 471],[522, 169],[715, 482]])      # Find Corner points
Width= 800
Height= 900
point2= np.float32([[0, 0],[800, Width],[0, Height],[Width, Height]])


matrix= cv.getPerspectiveTransform(point1, point2)
out_img= cv.warpPerspective(img, matrix, (Width, Height))

# Save image
cv.imwrite("Resources\Transform_img.jpg", out_img)

# Display:
cv.imshow("First image", img)
cv.imshow("Transform image", out_img)


cv.waitKey(0)
cv.destroyAllWindows()