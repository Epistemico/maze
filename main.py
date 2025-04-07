from graphics import *
from cell import *
from maze import *


def main():
    screen_x = 800
    screen_y = 600
    win = Window(screen_x, screen_y)
    
    num_rows = 10
    num_colums = 12

    # Centers grid with margin in GUI
    margin = 50
    cell_size_x = (screen_x - 2 * margin) / num_colums
    cell_size_y = (screen_y - 2 * margin) / num_rows
    maze = Maze(margin, margin, num_rows, num_colums, cell_size_x, cell_size_y, win)

    win.wait_for_close()


main()