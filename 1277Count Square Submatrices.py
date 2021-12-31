# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        
        result = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        result+=1
                    else:
                        matrix[i][j]+= min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])
                        result+=matrix[i][j]
        # print(matrix)
        
        return result