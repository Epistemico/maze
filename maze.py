from cell import Cell
import time


class Maze():
    def __init__(
        self, 
        x1, 
        y1, 
        num_rows, 
        num_cols, 
        cell_size_x, 
        cell_size_y, 
        window=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._create_cells()

    def _create_cells(self):
        # Cells are created and rendered vertically [column][row]
        for i in range(self._num_cols):
            cell_cols = []
            for j in range(self._num_rows):
                cell_cols.append(Cell(self._window))
            self._cells.append(cell_cols)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        self._cells[0][0].left_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].right_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _draw_cell(self, i, j):
        if self._window is None:
            return
        x1_coord = self._x1 + (self._cell_size_x * i)
        y1_coord = self._y1 + (self._cell_size_y * j)
        x2_coord = x1_coord + self._cell_size_x
        y2_coord = y1_coord + self._cell_size_y
        self._cells[i][j].draw(x1_coord, y1_coord, x2_coord, y2_coord)
        self._animate()

    def _animate(self):
        if self._window is None:
            return
        self._window.redraw()
        time.sleep(0.05)
