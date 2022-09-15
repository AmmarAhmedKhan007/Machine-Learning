
import cv2 as cv
import numpy as np

cap= cv.VideoCapture(0)
# Resolution:
cap.set(3, 1280)
cap.set(4, 720)
# 2nd method
def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)
hd_resolution()


# Play Video
while (True):
    (ret, frame)= cap.read()
    if ret == True:
        cv.imshow("Origional",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):      # To Stop Video
            break
    else:
        break

cap.release()
cv.destroyAllWindows