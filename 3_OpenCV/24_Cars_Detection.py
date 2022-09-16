
import cv2 as cv

cap = cv.VideoCapture('Resources\mixkit.mp4')
car_cascade = cv.CascadeClassifier('Resources\cars.xml')

while True:
    ret, frames = cap.read()
    gray = cv.cvtColor(frames, cv.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 9)
    # if str(np.array(cars).shape[0]) == '1':
    #     i += 1
    #     continue
    for (x,y,w,h) in cars:
        plate = frames[y:y + h, x:x + w]
        cv.rectangle(frames,(x,y),(x +w, y +h) ,(51 ,51,255),2)
        cv.rectangle(frames, (x, y - 40), (x + w, y), (51,51,255), -2)
        cv.putText(frames, 'Car', (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv.imshow('car',plate)

    # lab1 = "Car Count: " + str(i)
    # cv2.putText(frames, lab1, (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (147, 20, 255), 3)
    frames = cv.resize(frames,(600,400))
    cv.imshow('Car Detection System', frames)
    # cv2.resizeWindow('Car Detection System', 600, 600)
    if cv.waitKey(1) & 0xFF == ord('q'):      # To Stop Video
        break
cv.destroyAllWindows()