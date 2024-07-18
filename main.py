from display import *

def main():
        win = Display(800,600)  ##test lines draw
        testDraw(win)
        win.waitForClose()



def testDraw(win):
        line1 = Line(Point(11,500),Point(41, 120))
        line2 = Line(Point(115,520),Point(640, 100))
        line1.draw(win.canvas)
        line2.draw(win.canvas,"blue")


main()
