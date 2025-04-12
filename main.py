from graphics import Window
from maze import Maze
import sys


def main():
    screen_x = 800
    screen_y = 600
    win = Window(screen_x, screen_y)
    sys.setrecursionlimit(10000)

    num_rows = 10
    num_colums = 12

    # Centers grid with margin in GUI
    margin = 50
    cell_size_x = (screen_x - 2 * margin) / num_colums
    cell_size_y = (screen_y - 2 * margin) / num_rows

    # seed=int in Maze for fixed route
    maze = Maze(margin, margin, num_rows, num_colums, cell_size_x, cell_size_y, win)
    
    solvable = maze.solve()
    if not solvable:
        print("Maze can't be solved.")
    else:
        print("Maze solved!")

    win.wait_for_close()


main()