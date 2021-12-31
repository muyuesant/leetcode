# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        newInter = intervals.pop(0)
        
        result = []
        
        for interval in intervals:
            if newInter[1] == interval[0] or newInter[1] > interval[0]:
                newInter[1] = max(newInter[1], interval[1])
            else:
                result.append(newInter)
                newInter = interval
        result.append(newInter)
        return result