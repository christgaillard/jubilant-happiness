import numpy as np
import cv2
import RPi.GPIO as GPIO
import time, sys

cap = cv2.VideoCapture(0)

sound_speed = 340.0 / 1000
trigger_pin_left = 8
echo_pin_left = 7

trigger_pin_right=18
echo_pin_right = 23

GPIO.setmode (GPIO.BCM)
GPIO.setup(trigger_pin_right, GPIO.OUT)
GPIO.setup(echo_pin_right, GPIO.IN)

def send_trigger_pulse(pin):
    GPIO.output(pin, True)
    time.sleep(0.00001)
    GPIO.output(pin,False)
    
def wait_for_echo(pin, value, timeout):
    count = timeout
    while GPIO.input(pin) != value and count > 0:
        count  -= 1

def get_distance(trigger_pin, echo_pin):
    send_trigger_pulse(trigger_pin)
    wait_for_echo(echo_pin, True, 250000)
    start = time.time()
    wait_for_echo(echo_pin, False,250000)
    finish = time.time()
    pulse_len = finish - start
    distance_cm = pulse_len * 34000
    distance_cm = distance_cm/2
    return int(distance_cm)

green = (0, 255, 0)
orange = (0, 255, 255)
red = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #left_distance = get_distance(trigger_pin_lefft, echo_pin_left)
    right_distance = get_distance(trigger_pin_right,echo_pin_right) 


    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.line(frame, (50, 450), (550, 450), red, 5)
    cv2.line(frame,(50,450),(100,400),red,5)
    cv2.line(frame,(550,450),(500,400),red,5)
    cv2.line(frame,(90,400),(110,400),red,3)
    cv2.line(frame, (490, 400), (510, 400), red, 3)
    cv2.line(frame,(100,397),(185,300),orange,5)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'distance Objet : '+ str(right_distance), (10, 400), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    
    # Display the resulting frame
    cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        GPIO.cleanup()
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
time.sleep(0.1)