
import cv2 as cv

vid = cv.VideoCapture("Resources\Video.mp4")

# Writing format, Codec, video writer object and file Output
frame_width= int(vid.get(3))
frame_height= int(vid.get(4))
out= cv.VideoWriter("Resources\Out_Video.mp4", cv.VideoWriter_fourcc('M','J','P','G'),10,(frame_width, frame_height),isColor=False)

# Play Video
while (True):
    (ret, frame)= vid.read()
    Gray= cv.cvtColor (frame, cv.COLOR_BGR2GRAY)        # Gray Conversion
    # To show in Player
    if ret == True:
        out.write(Gray)
        cv.imshow("Video",Gray)
        # To Quit Video
        if cv.waitKey(1) & 0xFF == ord('q'):      # To Stop Video
            break
    else:
        break


vid.release()
out.release()
cv.destroyAllWindows