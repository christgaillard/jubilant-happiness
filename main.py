import numpy as np
import cv2


cap = cv2.VideoCapture(0)

green = (0, 255, 0)
orange = (0, 255, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.line(frame, (50, 150), (550, 150), orange, 5)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'OpenCV', (10, 400), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    # Display the resulting frame
    cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()