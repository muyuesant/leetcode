
# https://leetcode.com/problems/jump-game-ii/
# think it as tree, each level has the value that level-1 can jump to
# e.g 
# 0 1 2 3 4 5 6
# 2 1 3 1 1 1 2
# will be like
# 2
# 1 3
# 1 1 1
# 1
# 2
class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return 0
        jumps = 0
        currR = 0
        currMax = 0
        
        for i in range(size):
            currMax = max(currMax, nums[i]+i)
            if i == currR :
                jumps+=1
                currR = currMax
                if currMax == size - 1:
                    break
            
        return jumps