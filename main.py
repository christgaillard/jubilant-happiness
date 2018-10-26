import numpy as np
import cv2


cap = cv2.VideoCapture(0)

green = (0, 255, 0)
orange = (0, 255, 255)
red = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.line(frame, (50, 450), (550, 450), red, 5)
    cv2.line(frame,(50,450),(100,400),red,5)
    cv2.line(frame,(550,450),(500,400),red,5)
    cv2.line(frame,(90,400),(110,400),red,3)
    cv2.line(frame, (490, 400), (510, 400), red, 3)
    cv2.line(frame,(100,397),(185,300),orange,5)
    #font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(frame, 'OpenCV', (10, 400), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    # Display the resulting frame
    cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()