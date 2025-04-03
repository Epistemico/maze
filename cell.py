from graphics import Point, Line


class Cell():
    def __init__(self, window):
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
        self._x1_coord = x1
        self._y1_coord = y1
        self._x2_coord = x2
        self._y2_coord = y2
        if self.left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line)
        if self.right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line)
        if self.top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line)
        if self.bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line)
