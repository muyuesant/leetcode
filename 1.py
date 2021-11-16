# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        indexMap = {}
        for i in range(size):
            if nums[i] in indexMap:
                return [indexMap[nums[i]], i]
            else:
                indexMap[target - nums[i]] = i