
import numpy as np
import cv2 as cv

# 1-Load Image:
img= cv.imread("Resources\img.jpg")

# 2-Resize image:
resize_image= cv.resize(img, (500,500))   

# 3-Gray image:
gray_img= cv.cvtColor (resize_image, cv.COLOR_BGR2GRAY)  

# 4-Black & White image:
(thresh, b_w)= cv.threshold(resize_image, 127, 255, cv.THRESH_BINARY)

# 5-Blur Image:      
Blur_img= cv.GaussianBlur (resize_image,(7, 7), 0)

# 6-Edge Detection:
edge_img= cv.Canny(resize_image, 48,48)

# 7-Thickness of line of Edge detection
mat_kernel= np.ones((3,3),np.uint8)
dilated_img= cv.dilate(edge_img ,(mat_kernel), iterations=1)

# 8-thinner outline
ero_img= cv.erode(dilated_img, mat_kernel, iterations=1)

# 9-Crop Image:
print ("the Shape of Img is", img.shape)
Croped_img= img[500:1400, 500:800]



# Display:
cv.imshow("Origional", img)
cv.imshow("Reasize", resize_image)
cv.imshow("Gray", gray_img )
cv.imshow("Black_&_White", b_w )
cv.imshow("Blur", Blur_img )
cv.imshow("Edge", edge_img)
cv.imshow("dilated_img", dilated_img)
cv.imshow("Erode_img", ero_img)
cv.imshow("Erode_img", Croped_img)


cv.waitKey(0)
cv.destroyAllWindows()