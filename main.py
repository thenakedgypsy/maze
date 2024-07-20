from display import *
from geometry import *

def main():
        win = Display(800,600) 
        testDraw(win)
        win.waitForClose()



def testDraw(win):    ##test lines draw
        cell = Cell(Point(350,100),Point(380, 131))
        cell.draw(win.canvas)


main()
