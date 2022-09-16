
import cv2 as cv
import numpy as np

# Create Cascade
face_cascade= cv.CascadeClassifier('Resources\haarcascade_frontalface_default.xml')

cap = cv.VideoCapture('Resources\Ammar.mp4')

while (cap.isOpened()):
    ret, frame =cap.read()

    gray_img= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray_img, 1.1, 4)

# Draw rectangle
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x,y),(x+w, y+h),(255,0,0), 2)    

    cv.imshow("Videoo", frame)   
    if cv.waitKey(2) & 0xFF == ord('q'):      # To Stop Video
        break
cap.release()
cv.destroyAllWindows