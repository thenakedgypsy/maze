from tkinter import *

class Display(): #general display stuffs

    def __init__(self, width, height):   ##set up the display
        self.__root = Tk()
        self.__root.title("Maze")
        self.canvas = Canvas(self.__root,width=width, height=height)
        self.canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()   ##update the display
        self.__root.update()

    def waitForClose(self):
        self.__running = True
        while self.__running:           #keep the window open
            self.redraw()
    
    def close(self):
        self.__running = False                 #run away!


        



