
import cv2 as cv

vid = cv.VideoCapture(0)

# Writing format, Codec, video writer object and file Output
frame_width= int(vid.get(3))
frame_height= int(vid.get(4))
out= cv.VideoWriter("Resources\cam_Video.avi", cv.VideoWriter_fourcc('M','J','P','G'),20,(frame_width, frame_height))

# Play Video
while (True):
    (ret, frame)= vid.read()
    (thresh, b_w)= cv.threshold(frame, 127, 255, cv.THRESH_BINARY)    # Black & White Conversion
    # To show in Player
    if ret == True:
        out.write(b_w)
        cv.imshow("Black & White",b_w)
        # To Quit Video
        if cv.waitKey(1) & 0xFF == ord('q'):      # To Stop Video
            break
    else:
        break


vid.release()
out.release()
cv.destroyAllWindows