# https://leetcode.com/problems/number-of-provinces/
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        row = len(isConnected)
        if row == 1:
            return 1
        col = len(isConnected[0])
        
        queue = []
        
        result = 0
        for i in range(row):
            if isConnected[i][i] == 0:
                continue
            result += 1
            queue.append(i)
            
            while queue:
                root = queue.pop(0)
                if isConnected[root][root] == 0:
                    continue
                isConnected[root][root] = 0
                for j in range(col):
                    if isConnected[root][j] == 1:
                        isConnected[root][j] = 0
                        queue.append(j)
        
        return result  
                    
        