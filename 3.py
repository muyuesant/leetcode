# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenMap = {}
        left = 0
        res = 0
        for right in range(len(s)):
            
            if s[right] not in seenMap:
                # If s[rright] not in seen, increasing the window size by moving right pointer
                res = max(res, right-left+1)
            elif seenMap[s[right]] < left: 
                    # a[ b c ] a
                    res = max(res, right-left+1)
            else:
                # [a b c] a
                left = seenMap[s[right]] + 1
            seenMap[s[right]] = right
        return res
                