from geometry import *


class Maze():

    def __init__(self,x,y,numRows,numCols,cellSizeX,cellSizeY):
        self.__numRows = numRows
        self.__numCols = numCols
        self.__x = x
        self.__y = y
        self.__cellSizeX = cellSizeX
        self.__cellSizeY = cellSizeY
        self.__cells = []
        self.__createCells()


    def __createCells(self):
        x1 = self.__x
        x2 = self.__x + self.__cellSizeX
        y1 = self.__y
        y2 = self.__y + self.__cellSizeY
        i = 0
        while i < self.__numCols:
            self.__cells.append([])
            j = 0
            while j < self.__numRows:
                self.__cells[i].append(Cell(Point(x1,y1),Point(x2,y2)))
                
                y1 = y1 + self.__cellSizeY
                y2 = y2 + self.__cellSizeY
                j+=1
            y1 = self.__y
            y2 = self.__y + self.__cellSizeY    
            x1 = x1 + self.__cellSizeX
            x2 = x2 + self.__cellSizeX
            i += 1 


    def drawCells(self,canvas):
        for col in self.__cells:
            for cell in col:
                cell.draw(canvas)