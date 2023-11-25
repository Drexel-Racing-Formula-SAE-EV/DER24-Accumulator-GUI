import serial
import GlobalVariables
import threading

class Reader(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        

    def read(self):
        ser = serial.Serial(GlobalVariables.COM_PORT, baudrate= GlobalVariables.BAUD_RATE, timeout=1)
        # ser.write(b"Hello. Testing")
        while True:
            if ser.in_waiting:
                line = ser.readline(ser.in_waiting)
                self.queue.put(line)