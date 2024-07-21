import unittest
from maze import Maze

class Tests(unittest.TestCase):

    def test_Maze_CreateCells(self):
        numCols = 12
        numRows = 10
        m1 = Maze(0, 0, numRows, numCols, 10, 10)
        self.assertEqual(len(m1.cells),numCols)
        self.assertEqual(len(m1.cells[0]),numRows)

    def test_Maze_CreateCells_Many(self):
        numCols = 900
        numRows = 100
        m1 = Maze(0, 0, numRows, numCols, 10, 10)
        self.assertEqual(len(m1.cells),numCols)
        self.assertEqual(len(m1.cells[0]),numRows)

    def test_Maze_CreateCells_0Rows(self):
        numCols = 10
        numRows = 0
        with self.assertRaises(Exception):
            m1 = Maze(0, 0, numRows, numCols, 10, 10)
    
    def test_Maze_CreateCells_0Cols(self):
        numCols = 0
        numRows = 10
        with self.assertRaises(Exception):
            m1 = Maze(0, 0, numRows, numCols, 10, 10)

    def test_Maze_CreateCells_0Both(self):
        numCols = 0
        numRows = 0
        with self.assertRaises(Exception):
            m1 = Maze(0, 0, numRows, numCols, 10, 10)

    def test_Maze_CreateCells_Entrance(self):
        numCols = 10
        numRows = 10
        m1 = Maze(0, 0, numRows, numCols, 10, 10)
        assert m1.cells[0][0].walls["top"] == False

    def test_Maze_CreateCells_Exit(self):
        numCols = 10
        numRows = 99
        m1 = Maze(0, 0, numRows, numCols, 10, 10)
        assert m1.cells[-1][-1].walls["bottom"] == False

    def test_Visited_Reset(self):
        numCols = 10
        numRows = 10
        m1 = Maze(0, 0, numRows, numCols, 10, 10)
        m1.breakWallsR()
        m1.resetCellsVisited()
        visited = False
        for col in m1.cells:
            for cell in col:
                visited = cell.visited
        assert visited == False
                



if __name__ == "__main__":
    unittest.main()