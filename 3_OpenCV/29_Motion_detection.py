
import cv2 as cv
import numpy as np

cap = cv.VideoCapture("Resources\Ammar.mp4")
frame_width = int( cap.get(cv.CAP_PROP_FRAME_WIDTH))

frame_height =int( cap.get( cv.CAP_PROP_FRAME_HEIGHT))

fourcc = cv.VideoWriter_fourcc('X','V','I','D')

out = cv.VideoWriter("Resources\output.mp4", fourcc, 5.0, (1280,720))

ret, frame1 = cap.read()
ret, frame2 = cap.read()
print(frame1.shape)
while cap.isOpened():
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)

        if cv.contourArea(contour) < 900:
            continue
        cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    image = cv.resize(frame1, (1280,720))
    out.write(image)
    cv.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv.waitKey(1) & 0xFF == ord('q'):      # To Stop Video
        break

cv.destroyAllWindows()
cap.release()
out.release()