import serial


class lecture:
    def __init__(self, port, bauds):
        self.serialread = serial.Serial(port, bauds)  # /dev/ttyACM0', 115200
