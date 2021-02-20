import numpy as np
import math

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.make_square()
        self.repr = [[0]*self.cols for _ in range(self.rows)]

    def make_square(self):
        self.rows = self.cols if self.rows < self.cols else self.rows
        self.cols = self.rows if self.cols < self.rows else self.cols

    def paint(self, row, col):
        self.repr[row][col] = 1

    def erase(self, row, col):
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                self.repr[i][j] = 0

    def get_coords(self, x, y, w, h):
        px_per_unit = w//self.rows
        row, col = x//px_per_unit, y//px_per_unit
        return (row, col)