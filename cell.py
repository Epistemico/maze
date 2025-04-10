from graphics import Point, Line


class Cell():
    def __init__(self, window=None):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self._x1_coord = None
        self._y1_coord = None
        self._x2_coord = None
        self._y2_coord = None
        self._window = window
    
    def draw(self, x1, y1, x2, y2):
        if self._window is None:
            return
        
        self._x1_coord = x1
        self._y1_coord = y1
        self._x2_coord = x2
        self._y2_coord = y2
        
        if self.left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line, "white")
        
        if self.right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line, "white")
        
        if self.top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line, "white")
        
        if self.bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        x1_center = (self._x1_coord + self._x2_coord) / 2
        y1_center = (self._y1_coord + self._y2_coord) / 2
        x2_center = (to_cell._x1_coord + to_cell._x2_coord) / 2
        y2_center = (to_cell._y1_coord + to_cell._y2_coord) / 2
        
        fill_color = "red" if undo else "gray"
        line = Line(Point(x1_center, y1_center), Point(x2_center, y2_center))
        
        self._window.draw_line(line, fill_color)
