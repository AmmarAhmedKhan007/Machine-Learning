
import cv2 as cv

vid = cv.VideoCapture("Resources/Video.mp4")

frameno = 0

while (True):
    success, frame= vid.read()
    # To show in Player
    if success:
        cv.imwrite(f"Resources/frames/frame_{frameno}.jpg",frame)  
    else:
        break
    frameno= frameno+1
vid.release()