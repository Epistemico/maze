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


if __name__ == "__main__":
    unittest.main()
