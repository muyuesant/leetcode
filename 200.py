# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i: int, j: int, grid: List[List[str]], visit: List[List[bool]]):
            # print(i,j)
            visit[i][j] = True
            if i-1 > -1 and grid[i-1][j] == "1" and not visit[i-1][j]:
                dfs(i-1, j, grid, visit)
            if i+1 < len(grid) and grid[i+1][j] == "1" and not visit[i+1][j]:
                dfs(i+1, j, grid, visit)
                
            if j-1 > -1 and grid[i][j-1] == "1" and not visit[i][j-1]:
                dfs(i, j-1, grid, visit)
            if j+1 < len(grid[0]) and grid[i][j+1] == "1" and not visit[i][j+1]:
                dfs(i, j+1, grid, visit)
                
        row = len(grid)
        col = len(grid[0])
        result = 0
        visit = [[False for j in range(col)] for i in range(row) ]
        # print(visit)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and not visit[i][j]:
                    # print(visit)
                    result+=1
                    dfs(i, j, grid, visit)
        return result
        