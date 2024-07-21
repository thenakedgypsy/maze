from geometry import *
from random import *


class Maze():

    def __init__(self,x,y,numRows,numCols,cellSizeX,cellSizeY,seed = None):
        self.__numRows = numRows
        self.__numCols = numCols
        self.__x = x
        self.__y = y
        self.__cellSizeX = cellSizeX
        self.__cellSizeY = cellSizeY
        self.cells = []
        if self.seed is not None:
            self.seed = random.seed(seed)
        else:
            self.seed = 0
        self.__createCells()


    def __createCells(self):
        if self.__numRows == 0 or self.__numCols == 0:
            raise Exception("Maze must have rows and columns")
        x1 = self.__x
        x2 = self.__x + self.__cellSizeX
        y1 = self.__y
        y2 = self.__y + self.__cellSizeY
        i = 0
        while i < self.__numCols:
            self.cells.append([])
            j = 0
            while j < self.__numRows:               ##add each cell in row
                self.cells[i].append(Cell(Point(x1,y1),Point(x2,y2)))
                
                y1 = y1 + self.__cellSizeY
                y2 = y2 + self.__cellSizeY
                j+=1
            y1 = self.__y                           ##reset Y values to return to top of column
            y2 = self.__y + self.__cellSizeY    
            x1 = x1 + self.__cellSizeX
            x2 = x2 + self.__cellSizeX                ##adjust the X values to push along to next column
            i += 1 
        self.__breakEntranceAndExit()

    def drawCells(self,win):
        for col in self.cells:
            for cell in col:
                cell.draw(win.canvas)
                self.__animate(win)
        

    def __animate(self,win):
        win.canvas.after(50,win.redraw())

    def __breakEntranceAndExit(self):
        self.cells[0][0].hasTopWall = False
        self.cells[-1][-1].hasBottomWall = False