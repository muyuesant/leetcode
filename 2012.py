class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        size = len(nums)
        result = 0
        rightMin = [0] * size
        
        rightMin[size-1] = nums[size-1]
        
        for i in range(size-2, 1, -1):
            rightMin[i]=rightMin[i+1]
            if nums[i] < rightMin[i]:
                rightMin[i]=nums[i]
        # print(rightMin)
        
        leftMax = nums[0]
        for i in range (1, size-1):
            if nums[i] > leftMax and nums[i] < rightMin[i+1]:
                result += 2
                
            elif nums[i] > nums[i-1] and nums[i] < nums[i+1]:
                result += 1
            if nums[i] > leftMax:
                leftMax = nums[i]
        return result
