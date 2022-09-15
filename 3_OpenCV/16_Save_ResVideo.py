
import cv2 as cv
import numpy as np

cap= cv.VideoCapture(0)
# Resolution:
def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)
hd_resolution()

# Writing format, Codec, video writer object and file Output
frame_width= int(cap.get(3))
frame_height= int(cap.get(4))
out= cv.VideoWriter("Resources\Hd_Video.avi", cv.VideoWriter_fourcc('M','J','P','G'),20,(frame_width, frame_height))

# Play Video
while (True):
    (ret, frame)= cap.read()
    #(thresh, b_w)= cv.threshold(frame, 127, 255, cv.THRESH_BINARY)    # Black & White Conversion
    # To show in Player
    if ret == True:
        out.write(frame)
        cv.imshow("Black & White",frame)
        # To Quit Video
        if cv.waitKey(1) & 0xFF == ord('q'):      # To Stop Video
            break
    else:
        break


cap.release()
out.release()
cv.destroyAllWindows