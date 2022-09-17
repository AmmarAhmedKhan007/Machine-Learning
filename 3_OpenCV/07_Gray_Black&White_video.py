
import cv2 as cv

vid = cv.VideoCapture("Resources\Video.mp4")


# Play Video
while (True):
    (ret, frame)= vid.read()
    Gray= cv.cvtColor (frame, cv.COLOR_BGR2GRAY)        # Gray Conversion
    (thresh, b_w)= cv.threshold(Gray, 127, 255, cv.THRESH_BINARY)    # Black & White Conversion
    # To show in Player
    if ret == True:
        cv.imshow("Video",b_w)
        # To Quit Video
        if cv.waitKey(1) & 0xFF == ord('q'):      # To Stop Video
            break
    else:
        break


vid.release()
cv.destroyAllWindows