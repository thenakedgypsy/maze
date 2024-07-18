from tkinter import *




class Display():

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze"
        self.canvas = Canvas(self.__root)
        self.canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def waitForClose(self):
        self.__running = True
        if self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False

display = Display(1330, 14440)