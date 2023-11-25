import tkinter as tk
from tkinter import *
from tkinter import messagebox
from SegmentScreen.DisplaySegments import DisplaySegments as Segments
import GlobalVariables
from UART.UARTConnection import UARTConnection

class App():
    #Basic setup of the app. Sets up the main canvas of the screen
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        
        self.root.title("AMU GUI")
        self.cv = tk.Canvas(self.root, height = GlobalVariables.SCREEN_HEIGHT, width = GlobalVariables.SCREEN_WIDTH, highlightthickness=0)
        self.cv.pack()

        # Doesn't do anything right now ... maybe for dark mode? Changes background
        self.cv.configure(bg="white")

        #Init each of the screens
        GlobalVariables.INFO_SCREENS["SegmentDisplay"] = Segments(self)

        #Start UART Connection Thread
        self.uartConnection = UARTConnection()
        self.uartConnection.connect()

        #COM PORT SELECTION
        self.com_port_selection()
        
        #Exit when Escape is hit
        self.root.bind("<Escape>", self.on_exit)

        self.root.mainloop()

    #The n is to handle an extra argument that is sent for some reason
    def on_exit(self, n):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.uartConnection.disconnect()
            self.root.destroy()

    def com_port_selection(self):
        options = []
        for i in range (0, 16):
            options.append("COM" + str(i))

        self.clicked = StringVar(master=self.root)
        self.clicked.set(GlobalVariables.COM_PORT)
        dropdown = OptionMenu(self.cv, self.clicked, *options)
        dropdown.place(x=GlobalVariables.SCREEN_WIDTH - 200, y = 25)
        
        self.clicked.trace("w", self.updateCOMPort)

    def updateCOMPort(self, *args):
        GlobalVariables.COM_PORT = self.clicked.get()
        self.uartConnection.connect()

if __name__ == "__main__":
    app = App()
