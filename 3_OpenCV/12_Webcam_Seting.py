
import cv2 as cv
import numpy as np

# Read frame from Camera
cap= cv.VideoCapture(0)
cap.set (10, 50)   # 10 is Bightness key  # 50 is %
cap.set (3, 640)    # 3 is width
cap.set (4, 480)    # 4 is height


while (cap.isOpened()):
    ret, frame =cap.read()
    if ret == True:
        cv.imshow("Video",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):      # To Stop Video
            break
    else:
        break

cap.release()
cv.destroyAllWindows