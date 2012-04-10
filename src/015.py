#!/usr/bin/env python

def euler_15(grid_size):
    g = Grid(grid_size)
    return g.path_count()

class Grid():
    def __init__(self, grid_size):
        self.grid_size = grid_size

    def path_count(self):
        self.grid = [0] * (self.grid_size + 1)
        self.grid = [[0] * (self.grid_size + 1) for x in self.grid]
        self.grid[0][0] = 1

        self.cache = {}

        return self._path_count_from_point(0, 0, '')

    def _path_count_from_point(self, x, y, last_dir):
        if (x == self.grid_size and y == self.grid_size):
            return 0

        if (x, y) in self.cache:
            return self.cache[(x, y)]

        if x < self.grid_size:
            can_move_right = True
        else:
            can_move_right = False

        if y < self.grid_size:
            can_move_down = True
        else:
            can_move_down = False

        retval = 0

        if can_move_right:
            self.grid[x + 1][y] = 1
            retval += self._path_count_from_point(x + 1, y, 'R')

            if can_move_down and last_dir != 'R':
                retval += 1

        if can_move_down:
            self.grid[x][y + 1] = 1
            retval += self._path_count_from_point(x, y + 1, 'D')

            if can_move_right and last_dir != 'D':
                retval += 1

        if can_move_right and can_move_down:
            #only set the cache for non borders.
            #border counts are different depending on direction
            self.cache[(x, y)] = retval

        return retval

if __name__ == "__main__":
    print(euler_15(20))
