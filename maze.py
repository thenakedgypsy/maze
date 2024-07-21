from geometry import *
import random


class Maze():

    def __init__(self,x,y,numRows,numCols,cellSizeX,cellSizeY,seed = None):
        self.__numRows = numRows
        self.__numCols = numCols
        self.__x = x
        self.__y = y
        self.__cellSizeX = cellSizeX
        self.__cellSizeY = cellSizeY
        self.cells = []
        if seed is not None:
            random.seed(seed)

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
        self.cells[0][0].walls["top"] = False
        self.cells[-1][-1].walls["bottom"] = False

    
    def breakWallsR(self,col=0,row=0):
        self.cells[col][row].visited = True #this cell is now marked as visited
            
        while True:     #until all cells around this one are visited
            toVisit = []    ##will contain potential directions as: col, row, wall to remove on current cell, wall to remove on next cell
            if row -1 >= 0 and self.cells[col][row - 1].visited == False:   #checks up
                   toVisit.append((col,row-1,"top","bottom"))             #if unvisited adds to potential directions
            if row +1 < len(self.cells[col]) and self.cells[col][row + 1].visited == False: #checks down
                   toVisit.append((col,row+1,"bottom","top"))           #if unvisited adds to potential directions
            if col -1 >= 0 and self.cells[col-1][row].visited == False:     #checks left
                   toVisit.append((col-1,row,"left","right"))               #if unvisited adds to potential directions
            if col +1 < len(self.cells) and self.cells[col+1][row].visited == False: #checks right
                   toVisit.append((col+1,row,"right","left"))               #if unvisited adds to potential directions
            if not toVisit: #all surrounding cells visisted, end recursion
               return 
           
            nextCell = random.choice(toVisit)                       ##randomise which direction
            nextCol, nextRow, wallBreak, nextWall = nextCell        ##set some variables for clarity

            self.cells[col][row].walls[wallBreak] = False           ##break wall on current
            self.cells[nextCol][nextRow].walls[nextWall] = False        ##break wall on next
            
            self.breakWallsR(nextCol,nextRow)      ##call recursively on next cell

    def resetCellsVisited(self):
         for col in self.cells:
              for cell in col:
                   cell.resetVisited()


