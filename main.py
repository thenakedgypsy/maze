from display import *
from geometry import *
from maze import Maze

def main():
        win = Display(800,600) 
        testDraw(win)
        win.waitForClose()



def testDraw(win):    ##test lines draw
        maze = Maze(45,35,12,16,45,45) ##draws a grid using cells
        maze.breakWallsR(0,0,win)
        maze.drawCells(win)
        
main()
