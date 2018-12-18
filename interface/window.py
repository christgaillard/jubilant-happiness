import tkinter
import PIL.Image, PIL.ImageTk
import video.capture as cap
import tkinter.font as tkFont


class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        #self.photo = tkinter.PhotoImage(file='images/bt_fermer.gif')
        self.helv22 = tkFont.Font(family='Helvetica', size=22, weight=tkFont.BOLD)

        self.vid = cap.MyvideoCapture(self.video_source)

        self.bouton= tkinter.Button(window, text="Fermer", font=self.helv22, cursor='hand1', command=window.quit)
        self.bouton.pack()

        self.canvas = tkinter.Canvas(window, width=850, height=600)
        self.canvas.pack()

        self.delay = 15
        self.update()

        self.window.mainloop()

    def update(self):
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        self.window.after(self.delay, self.update)

