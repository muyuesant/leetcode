# https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in intervals:
            if newInterval is None or i[1] < newInterval[0]:
                result.append(i)
            elif i[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = None
                result.append(i)
            else:
#                 merge i and newInterval
                newInterval[0] = min(i[0], newInterval[0])
                newInterval[1] = max(i[1], newInterval[1])
    
        if newInterval is not None:
            result.append(newInterval)
        
        return result