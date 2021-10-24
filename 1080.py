class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if i * j == 0 or i == row-1 or j == col -1:
                    self.dfs(grid, i, j, row, col)
        result = 0
        for i in range(row):
            for j in range(col):
                result += grid[i][j]
        return result
    
    def dfs(self, grid: List[List[int]], i: int, j: int, row: int, col: int):
        
        if i < 0 or  j < 0 or i == row or j == col or grid[i][j] == 0:
            return
        grid[i][j] = 0
        self.dfs(grid, i,   j+1, row, col) # east
        self.dfs(grid, i+1, j, row, col) # south
        self.dfs(grid, i,   j-1, row, col) # west
        self.dfs(grid, i-1, j, row, col) # north