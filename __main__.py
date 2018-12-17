#!/usr/bin/python
from PIL import ImageFont, ImageDraw, Image
import cv2
import time, sys
#import serial
import numpy as np

text_to_show = "The quick brown fox jumps over the lazy dog"
image = cv2.imread("images/650602main_pia15415-43.jpg")
# Convert the image to RGB (OpenCV uses BGR)
cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Pass the image to PIL
pil_im = Image.fromarray(cv2_im_rgb)

draw = ImageDraw.Draw(pil_im)
# use a truetype font
font = ImageFont.truetype("fonts/Roboto/Roboto-Regular.ttf", 80)

# Draw the text
draw.text((10, 700), text_to_show, font=font)

# Get back the image to OpenCV
cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

cv2.imshow('Fonts', cv2_im_processed)
cv2.waitKey(0)

cv2.destroyAllWindows()




#ser = serial.Serial('/dev/ttyACM0', 115200)

cap = cv2.VideoCapture(0)

green = (0, 255, 0)
orange = (0, 255, 255)
red = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
cv2.namedWindow("video",cv2.WINDOW_NORMAL)
cv2.resizeWindow("video",600,400)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #read value from serial
   # val = str(ser.readline())
    #split them
    #a,b = val.split(":")
    #sanitize string to have only number and dots
    #a=a[2:]
    #b=b[:-5]
    #convert string to float.
    #dist1=float(a)
    #dist2=float(b)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    font = cv2.FONT_HERSHEY_SIMPLEX
    color = red
    cv2.line(frame,(100,500), (100,int(dist1)), color, 2)
    cv2.line(frame, (500, 500), (500, int(dist2)), color, 2)
    #cv2.putText(frame, 'distance1 Objet : '+ str(dist1), (10, 400), font, 1, color, 1, cv2.LINE_AA)
    #cv2.putText(frame, 'distance2 Objet : '+ str(dist2), (10, 440), font, 1, color, 1, cv2.LINE_AA)
    
    # Display the resulting frame
    #cv2.imshow('video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
           break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
time.sleep(0.1)