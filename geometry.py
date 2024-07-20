class Point(): #xy
    
    def __init__(self,x,y):       #init the xy       
        self.x = x
        self.y = y

class Line():  #for drawing out lines
    
    def __init__(self, point1, point2): #takes 2 xy points
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, colour="red"): #draws lines between points, in red if no color given
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=colour, )

class Cell():       #maze corners/boxes

    def __init__(self,topLeft, bottomRight):
        self.hasLeftWall = True
        self.hasRightWall = True
        self.hasTopWall = True
        self.hasBottomWall = True
        self.__topLeft = topLeft
        self.__bottomRight = bottomRight


    def draw(self,canvas):
        bottomLeft = Point(self.__topLeft.x,self.__bottomRight.y)
        topRight = Point(self.__bottomRight.x,self.__topLeft.y)
        if self.hasLeftWall:
            line = Line(bottomLeft,self.__topLeft)
            line.draw(canvas)
        if self.hasTopWall:
            line = Line(topRight,self.__topLeft)
            line.draw(canvas)
        if self.hasRightWall:
            line = Line(topRight,self.__bottomRight)
            line.draw(canvas)
        if self.hasBottomWall:
            line = Line(bottomLeft,self.__bottomRight)
            line.draw(canvas)