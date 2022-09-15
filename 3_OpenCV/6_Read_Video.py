
import cv2 as cv

vid = cv.VideoCapture("Resources\Video.mp4")

# Indicator
if (vid.isOpened() == False):
    print("Error in Reading Video")

# Play Video
while (vid.isOpened()):
    ret, frame =vid.read()
    if ret == True:
        cv.imshow("Video",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):      # To Stop Video
            break
    else:
        break

vid.release()
cv.destroyAllWindows