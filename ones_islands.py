
class Solution(object):
    def __init__(self, o_grid, b_grid, count):
        self.o_grid = o_grid
        self.b_grid = b_grid
        self.count = count

    def explore(self):
        h = len(self.o_grid)
        w = len(self.o_grid[0])

        for i in range(w):
            for j in range(h):
                if self.o_grid[i][j] == 1 and not self.b_grid[i][j]:
                    self.count = self.count + 1
                    self.explore_helper(i, j)
        return self.count

    def explore_helper(self, n, m):
        if (0 <= n < len(self.o_grid)) and (0 <= m < len(self.o_grid[0])):
            if self.o_grid[n][m] == 1 and not self.b_grid[n][m]:
                self.b_grid[n][m] = True
                self.explore_helper(n - 1, m - 1)
                self.explore_helper(n - 1, m)
                self.explore_helper(n - 1, m + 1)
                self.explore_helper(n, m + 1)
                self.explore_helper(n + 1, m + 1)
                self.explore_helper(n + 1, m)
                self.explore_helper(n + 1, m - 1)
                self.explore_helper(n, m - 1)


ones_zero_grid = [[1, 0, 1, 1, 0, 0],
                  [1, 0, 1, 1, 0, 0],
                  [0, 1, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 1],
                  [1, 0, 1, 0, 0, 1],
                  [1, 0, 1, 0, 0, 0]]

h = len(ones_zero_grid)
w = len(ones_zero_grid[0])
bool_grid = [[False for i in range(w)] for j in range(h)]

print(Solution(ones_zero_grid, bool_grid, 0).explore())
