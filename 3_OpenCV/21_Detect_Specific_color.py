
import cv2 as cv
from cv2 import cvtColor
import numpy as np

img= cv.imread("Resources\img.jpg")
img= cv.resize(img, (600,600))

# Convert into hsv (hue, saturation, value)
# hsv_img= cv.cvtColor (img, cv.COLOR_BGR2HSV)

# Slider
def slider():
    pass
path= "Resources\img.jpg"
cv.namedWindow("Bars")         # Open new window
cv.resizeWindow("Bars",700,300)

# Create Sliders
cv.createTrackbar("Min Hue","Bars",0,179, slider)               # The value of hue is 180
cv.createTrackbar("Max Hue","Bars",179,179, slider)  
cv.createTrackbar("Min Saturation","Bars",0,255, slider)  
cv.createTrackbar("Max Saturation","Bars",255,255, slider)  
cv.createTrackbar("Min Value","Bars",0,255, slider)  
cv.createTrackbar("Max Value","Bars",255,255, slider)  

cv.imread(path)
hsv_img= cv.cvtColor (img, cv.COLOR_BGR2HSV)

# hue_min= cv.getTrackbarPos("Min Hue","Bars")
# print(hue_min)

while (True):
    cv.imread(path)
    hsv_img= cv.cvtColor (img, cv.COLOR_BGR2HSV)

    Hue_min= cv.getTrackbarPos("Min Hue","Bars")
    Hue_max= cv.getTrackbarPos("Max Hue","Bars")
    Saturation_min= cv.getTrackbarPos("Min Saturation","Bars")
    Saturation_max= cv.getTrackbarPos("Max Saturation","Bars")
    Value_min= cv.getTrackbarPos("Min Value","Bars")
    Value_max= cv.getTrackbarPos("Max Value","Bars")

    print(Hue_min, Hue_max, Saturation_min, Saturation_max, Value_min, Value_max)

# See Changes inside an Image
    lower= np.array([Hue_min, Saturation_min, Value_min])
    upper= np.array([Hue_max, Saturation_max, Value_max])
    mask_img= cv.inRange(hsv_img, lower, upper)
    out_img= cv.bitwise_and(img, img, mask=mask_img)


    cv.imshow("Origional", img)
    cv.imshow("First image", hsv_img)
    cv.imshow("Mask Image", mask_img)
    cv.imshow("Final output", out_img)

    if cv.waitKey(1) & 0xFF == ord('q'):     
        break
cv.destroyAllWindows()


