import serial
import GlobalVariables
import threading
import GlobalVariables
import re

class UARTConnection():
    def __init__(self):
        self.ser = None
        self.stopFlag = True

    def connect(self):
        try:
            self.ser = serial.Serial(GlobalVariables.COM_PORT, baudrate= GlobalVariables.BAUD_RATE, timeout=1)
            thread = threading.Thread(target=self.receiveData)
            thread.daemon = True
            thread.start()
        except:
            print("COM Port could not be reached")

    def receiveData(self):
        while self.stopFlag:
            if self.ser.in_waiting:
                line = self.ser.readline(self.ser.in_waiting).decode("utf-8")
                self.processIncomingData(line)

    def sendData(self):
        pass

    def disconnect(self):
        self.stopFlag = False
        try:
            self.ser.close()
        except:
            print("Could not close serial")

    def processIncomingData(self, data):
        for (key, value) in GlobalVariables.UART_FORMATS.items():
            pattern = re.compile(value)
            (className, updateFunction) = key.split(".")
            if pattern.match(data):
                func = getattr(GlobalVariables.INFO_SCREENS[className], updateFunction)
                func(data)