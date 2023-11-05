import tkinter as tk
from tkinter import messagebox
from SegmentScreen.DisplaySegments import DisplaySegments as Segments
import GlobalVariables

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
        Segments(self)
        
        #Exit when Escape is hit
        self.root.bind("<Escape>", self.on_exit)

        self.root.mainloop()

    #The n is to handle an extra argument that is sent for some reason
    def on_exit(self, n):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
        
if __name__ == "__main__":
    app = App()
