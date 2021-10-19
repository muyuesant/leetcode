class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1:
            return matrix.pop(0)
        return matrix.pop(0)+self.spiralOrder(self.leftRotate(matrix))
    
    def leftRotate(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix[0])
        col = len(matrix)
        # print("row", row, "col",col)
        # print("matrix",matrix)
        result = [[0 for i in range(col)] for j in range(row)]
       
        for i in range(row):
            for j in range(col):
                result[i][j] = matrix[j][row-1-i]
        #         print(i,j)
        #         print(result)
        # print("result",result)
        return result