from graphics import *
from cell import *


def main():
    win = Window(800, 600)
    
    line = Line(Point(10, 10), Point(100, 110))
    line2 = Line(Point(10, 110), Point(100, 10))

    win.draw_line(line, "black")
    win.draw_line(line2, "red")
    
    cell = Cell(win)
    cell.top_wall = False
    cell.right_wall = False
    cell.draw(100, 10, 200, 110)

    cell2 = Cell(win)
    cell2.left_wall = False
    cell2.right_wall = False
    cell2.draw(200, 10, 300, 110)

    cell3 = Cell(win)
    cell3.left_wall = False
    cell3.right_wall = False
    cell3.draw(300, 10, 400, 110)

    cell4 = Cell(win)
    cell4.left_wall = False
    cell4.bottom_wall = False
    cell4.draw(400, 10, 500, 110)

    cell.draw_move(cell2)
    cell2.draw_move(cell3)
    cell3.draw_move(cell4)

    win.wait_for_close()


main()