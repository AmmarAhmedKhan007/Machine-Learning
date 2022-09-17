
import cv2 as cv
import numpy as np

# Read frame from Camera
cap= cv.VideoCapture(0)

print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 1000)
cap.set(4, 1000)

print(cap.get(3))
print(cap.get(4))

# Indicator
if (cap.isOpened() == False):
    print("Error in Reading Video")              # ptional

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