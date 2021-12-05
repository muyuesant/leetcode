# https://leetcode-cn.com/problems/meeting-rooms-ii/
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 1
        intervals.sort(key = lambda x: x[0] )
        temp=0
        while intervals:
            temp +=1
            preEnd = intervals.pop(0)[1]
            stack = []
            for m in intervals:
                if preEnd < m[0] or preEnd == m[0]:
                    preEnd = m[1]
                else:
                    stack.append(m)
            intervals = stack
            # print(intervals)
            # print(temp)
        return temp