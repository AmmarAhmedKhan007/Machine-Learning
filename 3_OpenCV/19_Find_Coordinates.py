
import cv2 as cv
import numpy as np

# Define function
def find_coord (event, x, y, flags, parms):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, '',y)      # Left mouse click
        # Define in Window
        font= cv.FONT_HERSHEY_PLAIN
        cv.putText(img, str(x)+','+str(y), (x,y), font, 1,(255,0,0), thickness=2)
        # Shoe text on Image
        cv.imshow("Image",img)

# For right click on image and show color values such as (b g r)
    if event == cv.EVENT_RBUTTONDOWN:
        print(x, '',y) 
        font= cv.FONT_HERSHEY_SIMPLEX
        b= img[y,x,0]
        g= img[y,x,1]
        r= img[y,x,2]
        cv.putText(img, str(b) + ',' + str(g)+ ',' + str(r), (x,y), font, 1,(255,0,0), thickness=2)
        cv.imshow("Image",img)

# Final function to read and display
if __name__ == "__main__":
    img= cv.imread("Resources\wrap.png",1)  # Read Image
    cv.imshow("Image", img)         # Display Image
    cv.setMouseCallback("Image", find_coord)      # Setting call back function
    cv.waitKey(0)
    cv.destroyAllWindows()