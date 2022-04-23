
class Solution(object):
    def __init__(self, o_grid, q_grid, count):
        self.o_grid = o_grid
        self.q_grid = q_grid
        self.queen_count = count

    def explore(self):
        h = len(self.o_grid)
        w = h

        for i in range(w):
            for j in range(h):
                if self.o_grid[i][j] == 1:
                    self.queen_count = self.queen_count + 1
                    self.explore_helper(i, j)
        self.q_grid[i][j] == self.queen_count
        return self.count

    def num_queen_find(self, q_grid):
        max_queen = 0
        for i in range(w):
            for j in range(h):
                if self.q_grid[i][j] >= max_queen:
                    max_queen == self.q_grid[i][j]
        return max_queen

    def explore_helper(self, n, m):
        if (0 <= n < len(self.o_grid)) and (0 <= m < len(self.o_grid[0])):
            if self.o_grid[n][m] == 1:
                self.q_grid[n][m] = True
                self.explore_helper(n - 1, m - 2)
                self.explore_helper(n - 2, m - 1)
                self.explore_helper(n - 1, m + 2)
                self.explore_helper(n + 1, m - 2)
                self.explore_helper(n + 2, m - 1)
                self.explore_helper(n + 2, m + 1)
                self.explore_helper(n + 1, m + 2)


ones_zero_grid = [[0, 1, 0, 0],
                  [0, 0, 0, 1],
                  [1, 0, 0, 0],
                  [0, 0, 1, 0]]

h = len(ones_zero_grid)
w = len(ones_zero_grid[0])
queens_grid = [[0 for i in range(w)] for j in range(h)]

print(Solution(ones_zero_grid, queens_grid, 0).explore())
print(Solution.num_queen_find(queens_grid))