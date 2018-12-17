#!/usr/bin/python
import tkinter
import PIL.Image, PIL.ImageTk
import cv2
import time, sys
import serial

ser = serial.Serial('/dev/ttyACM0', 115200)

cap = cv2.VideoCapture(0)



class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source


        self.vid = MyvideoCapture(self.video_source)

        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        self.delay = 15
        self.update()

        self.window.mainloop()


    def update(self):
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        self.window.after(self.delay, self.update)



class MyvideoCapture:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video")

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret :
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


# App(tkinter.Tk(), "Tkinter and OpenCV") appel de la class app



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
    val = str(ser.readline())
    #split them
    a,b = val.split(":")
    #sanitize string to have only number and dots
    a=a[2:]
    b=b[:-5]
    #convert string to float.
    dist1=float(a)
    dist2=float(b)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    font = cv2.FONT_HERSHEY_SIMPLEX
    color = red
    cv2.line(frame,(100,500), (100,int(dist1)), color, 2)
    cv2.line(frame, (500, 500), (500, int(dist2)), color, 2)
    cv2.putText(frame, 'distance1 Objet : '+ str(dist1), (10, 400), font, 1, color, 1, cv2.LINE_AA)
    cv2.putText(frame, 'distance2 Objet : '+ str(dist2), (10, 440), font, 1, color, 1, cv2.LINE_AA)
    
    # Display the resulting frame
    cv2.imshow('video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
           break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
time.sleep(0.1)