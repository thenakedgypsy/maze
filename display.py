from tkinter import *

class Display():

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze")
        self.canvas = Canvas(self.__root,width=width, height=height)
        self.canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def waitForClose(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line():
    
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, colour="red"):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=colour, )





