import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_maze_cell_size(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cell_size_x,
            10
        )
        self.assertEqual(
            m1._cell_size_y,
            10
        )

    def test_maze_create_large_cells(self):
        num_cols = 20
        num_rows = 15
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
        self.assertEqual(
            m1._cell_size_x,
            20
        )
        self.assertEqual(
            m1._cell_size_y,
            20
        )

    def test_maze_open_entrance_exit(self):
        # By default left wall of first cell and right wall of last cell are open.
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].left_wall,
            False
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].right_wall,
            False
        )

    def test_visited_reset(self):
        num_cols = 8
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 8, 8)
        for column in m1._cells:
            for cell in column:
                self.assertEqual(
                    cell.visited,
                    False
                )


if __name__ == "__main__":
    unittest.main()
