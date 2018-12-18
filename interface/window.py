import tkinter
import PIL.Image, PIL.ImageTk
import video.capture as cap
import tkinter.font as tkFont


class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # self.photo = tkinter.PhotoImage(file='images/bt_fermer.gif')
        self.helv22 = tkFont.Font(family='Helvetica', size=22, weight=tkFont.BOLD)

        self.vid = cap.MyvideoCapture(self.video_source)

        self.boutonClose= tkinter.Button(window, text="Fermer", font=self.helv22, cursor='hand1', command=window.quit)
        # self.boutonClose.pack(side="top", expand=False, padx=4, pady=4, anchor="w")
        self.boutonClose.grid(row=0, column=0)

        self.boutonShowLine = tkinter.Button(window, text='Line détection', font=self.helv22, cursor='hand1', command='')
        # self.boutonShowLine.pack(side="top", expand=False, padx=4, pady=4)
        self.boutonShowLine.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(window, width=800, height=480)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.delay = 15
        self.update()

        self.window.mainloop()

    def update(self):
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        self.window.after(self.delay, self.update)
