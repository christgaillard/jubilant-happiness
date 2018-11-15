import numpy as np
import cv2
import RPi.GPIO as GPIO
import time, sys
import serial
ser = serial.Serial('/dev/ttyACM0', 115200)

cap = cv2.VideoCapture(0)

green = (0, 255, 0)
orange = (0, 255, 255)
red = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
cv2.namedWindow("video",cv2.WINDOW_NORMAL)
cv2.resizeWindow("video",600,400)
#img = np.zeros((600,400,3), np.uint8)
counter = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    val = str(ser.readline())
    a,b = val.split(":")
    print(b)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   # py= int(450)-int(val)
   #cv2.line(frame, (50, py), (550, py), red, 5)
   # cv2.line(frame,(50,450),(100,400),red,5)
   # cv2.line(frame,(550,450),(500,400),red,5)
   # cv2.line(frame,(90,400),(110,400),red,3)
   # cv2.line(frame, (490, 400), (510, 400), red, 3)
   # cv2.line(frame,(100,397),(185,300),orange,5)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    #if(val>150):
     #   color = green
    #if(val<150):
    color = red
   # cv2.ellipse(frame, (400,py),(100,50),180,20,160,color,26,4)
    cv2.putText(frame, 'distance1 Objet : '+ str(a), (10, 400), font, 1, color, 1, cv2.LINE_AA)
    cv2.putText(frame, 'distance2 Objet : '+ str(b), (10, 440), font, 1, color, 1, cv2.LINE_AA)
    
    # Display the resulting frame
    cv2.imshow('video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        GPIO.cleanup()
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
time.sleep(0.1)