from cell import Cell
import time
import random


class Maze():
    def __init__(
        self, 
        x1, 
        y1, 
        num_rows, 
        num_cols, 
        cell_size_x, 
        cell_size_y, 
        window=None,
        seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window

        # Seed for maze path randomization
        if seed is not None:
            seed = random.seed(seed)
        # Initialize and render Maze
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
        self._cells[self._num_cols - 1][self._num_rows - 1].right_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        # Recursive Depth First Traversal of Maze to break walls
        # i-Columns (x axis), j-Rows (y axis)
        current = self._cells[i][j]
        current.visited = True
        while True:
            to_visit = []
            
            # Visit Left, Right, Up, Down
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            
            # No neighbors left in all 4 adjacent directions
            if not to_visit:
                self._draw_cell(i, j)
                return

            # Choose random neighboring cell
            next_i, next_j = to_visit[random.randrange(len(to_visit))]
            neighbor = self._cells[next_i][next_j]

            # Break walls between current and neighbor cell
            if next_i == i + 1:
                current.right_wall = False
                neighbor.left_wall = False
            if next_i == i - 1:
                current.left_wall = False
                neighbor.right_wall = False
            if next_j == j + 1:
                current.bottom_wall = False
                neighbor.top_wall = False
            if next_j == j - 1:
                current.top_wall = False
                neighbor.bottom_wall = False

            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

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
        time.sleep(0.03)
