from graphics import *


def main():
    win = Window(800, 600)
    
    line = Line(Point(10, 10), Point(200, 200))
    line2 = Line(Point(10, 200), Point(200, 10))

    win.draw_line(line, "black")
    win.draw_line(line2, "red")
    
    win.wait_for_close()


main()