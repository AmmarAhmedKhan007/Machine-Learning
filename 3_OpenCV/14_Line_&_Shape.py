
import cv2 as cv
import numpy as np

# Draw Canvas (Picture) using numpy
img= np.zeros((500, 500))     # zeros for Black
img1= np.ones((600, 600))    # ones for White

# Check Size
print("The size of Image is:", img.shape)

# Adding Colors:
Colored_img= np.zeros((600, 600, 3), np.uint8)    # 3 is color Channel
# Color full image:
Colored_img[:] =  255, 0, 255                     # [:] means ka Sari image  # 255, 0, 255 is color key
# Color Part of image:
Colored_img[200:400, 200:400] =  255, 0, 0 

# Adding Line:
Line =cv.line(Colored_img, (0,0), (600,600), (255,0,0), 3)

# Adding rectangle:
rectangle= cv.rectangle(Colored_img, (100,200),(300,500),(255,0,0),3)    # 3 is thickness
rectangle= cv.rectangle(Colored_img, (100,200),(300,500),(255,0,0),cv.FILLED)    # To fill triangle

# Adding Circle:
Circle= cv.circle(img, (300,300),100, (255,100,0), 10)
Circle= cv.circle(img, (300,300),100, (255,100,0), cv.FILLED)     # To fill Circle

# Adding Text:
Text= cv.putText(img,"Ammar Ahmed",(80,100),cv.FONT_HERSHEY_DUPLEX, 1.5,(255,100,0),3)


# Display:
cv.imshow("Black", img)
cv.imshow("White", img1)
cv.imshow("Colored_img", Colored_img)
cv.imshow("Line", Line)
cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", Circle)
cv.imshow("Texted_Image", Text)


cv.waitKey(0)
cv.destroyAllWindows()