from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__executing = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__executing = True
        while self.__executing:
            self.redraw()
        print("GUI closed")
    
    def close(self):
        self.__executing = False


class Point():
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y


class Line():
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point_1.x_coord, 
            self.point_1.y_coord, 
            self.point_2.x_coord, 
            self.point_2.y_coord, 
            fill=fill_color, 
            width=2
        )
