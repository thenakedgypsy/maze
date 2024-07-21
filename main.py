from display import *
from geometry import *
from maze import Maze
import random

def main():
        win = Display(800,600) 
        draw(win)
        win.waitForClose()



def draw(win):    ##test lines draw
        seed = random.randint(1,999999)
        print(seed)
        maze = Maze(45,35,12,16,45,45,826560) ##draws a grid using cells
        maze.breakWallsR()
        maze.drawCells(win)
        maze.resetCellsVisited()
        maze.solve(win)

        
main()
