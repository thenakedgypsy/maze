class Point(): #xy
    
    def __init__(self,x,y):       #init the xy       
        self.x = x
        self.y = y

class Line():  #for drawing out lines
    
    def __init__(self, point1, point2): #takes 2 xy points
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, colour="black"): #draws lines between points, in red if no color given
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=colour, )

class Cell():       #maze corners/boxes

    def __init__(self,topLeft, bottomRight, hasLeftWall=True,hasTopWall=True,hasRightWall=True,hasBottomWall=True):
        self.walls = {"left": hasLeftWall, "right": hasRightWall, "top": hasTopWall, "bottom": hasBottomWall}
        self.__topLeft = topLeft
        self.__bottomRight = bottomRight
        self.visited = False


    def draw(self,canvas):
        bottomLeft = Point(self.__topLeft.x,self.__bottomRight.y)
        topRight = Point(self.__bottomRight.x,self.__topLeft.y)
        if self.walls["left"]:
            line = Line(bottomLeft,self.__topLeft)
            line.draw(canvas)
        if self.walls["top"]:
            line = Line(topRight,self.__topLeft)
            line.draw(canvas)
        if self.walls["right"]:
            line = Line(topRight,self.__bottomRight)
            line.draw(canvas)
        if self.walls["bottom"]:
            line = Line(bottomLeft,self.__bottomRight)
            line.draw(canvas)

    def getCenter(self):
        centerX = (self.__topLeft.x + self.__bottomRight.x) / 2
        centerY = (self.__topLeft.y + self.__bottomRight.y) / 2
        return Point(centerX,centerY)


    def drawMove(self,win,toCell,undo=False,):
        fillColor = "green4"
        if undo:
            fillColor = "red"
        line = Line(self.getCenter(),toCell.getCenter())
        line.draw(win.canvas,fillColor)  

    def resetVisited(self):
        self.visited = False
