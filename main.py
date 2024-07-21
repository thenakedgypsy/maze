from display import *
from geometry import *
from maze import Maze

def main():
        win = Display(800,600) 
        testDraw(win)
        win.waitForClose()



def testDraw(win):    ##test lines draw
        maze = Maze(35,35,12,16,45,45)
        maze.drawCells(win.canvas)





#       cell = Cell(Point(150,100),Point(180, 131),hasRightWall=False)
#       cell.draw(win.canvas)
#       cell2 = Cell(Point(450,100),Point(480, 131),hasLeftWall=False)
#       cell2.draw(win.canvas)
#       cell.drawMove(win.canvas,cell2)
        
main()
