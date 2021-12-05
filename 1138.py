# https://leetcode.com/problems/alphabet-board-path/
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = "abcdefghijklmnopqrstuvwxyz"
        indexMap = {}
        for i,v in enumerate(board):
            indexMap[v] = [i//5, i%5]
        # print(indexMap)
        x = 0
        y = 0
        result = []
        for t in target:
            xt,yt = indexMap[t]
#             becase the last row has only "z", we need to do U and R first.
            if xt < x :
                result.append("U" * (x - xt) )
            if yt > y :
                result.append("R" * (yt - y) )
            
                
            if yt < y :
                result.append("L" * (y - yt) )
                
            if xt > x :
                result.append("D" * (xt - x) )
            
                
            
            result.append("!")
            x=xt
            y=yt
        
        return "".join(result)
            