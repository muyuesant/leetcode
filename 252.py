# https://leetcode.com/problems/meeting-rooms-ii/
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True
        intervals.sort(key = lambda x: x[0] )
        preEnd = intervals.pop(0)[1]
        for m in intervals:
            if preEnd > m[0]:
                return False
            else:
                preEnd = m[1]
        return True
