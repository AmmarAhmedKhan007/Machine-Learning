
import cv2 as cv
import numpy as np

cap= cv.VideoCapture(0)

# Play Video
while (True):
    (ret, frame)= cap.read()
    Gray= cv.cvtColor (frame, cv.COLOR_BGR2GRAY)        # Gray Conversion
    (thresh, b_w)= cv.threshold(Gray, 127, 255, cv.THRESH_BINARY)    # Black & White Conversion
    if ret == True:
        cv.imshow("Origional",frame)        # Show Origional Video
        cv.imshow("Gray",Gray)              # Show Gray Video
        cv.imshow("Black & White",b_w)      # Show Black & White Video

        if cv.waitKey(1) & 0xFF == ord('q'):      # To Stop Video
            break
    else:
        break

cap.release()
cv.destroyAllWindows