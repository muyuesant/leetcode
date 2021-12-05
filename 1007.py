# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        nums = [None for i in range(7)]
        numMap = {}
        size= len(tops)
        for i in range(size):
            if tops[i]  != bottoms[i]:
                if tops[i] not in numMap:
                    numMap[tops[i]] = 1
                else:
                    numMap[tops[i]] += 1
                
                if bottoms[i] not in numMap:
                    numMap[bottoms[i]] = 1
                else:
                    numMap[bottoms[i]] += 1
            else:
                if bottoms[i] not in numMap:
                    numMap[bottoms[i]] = 1
                else:
                    numMap[bottoms[i]] += 1
        
        
        for i in numMap.keys():
            if numMap[i] < size:
                continue
            swap2Top =0
            swap2Bot = 0
            isGood = True
            for j in range(size):
                if tops[j] == i and bottoms[j] == i:
                    continue
                elif tops[j] != i and bottoms[j] != i:
                    isGood = False
                    nums[i] = None
                    break
                elif tops[j] == i:
                    swap2Bot += 1
                elif bottoms[j] == i:
                    swap2Top += 1
            if isGood:
                nums[i] = min(swap2Bot, swap2Top)
            
        nums = list(filter(lambda x: x is not None,nums))
        # print(nums)
        if len(nums) > 0:
            return min(nums)
        else:
            return -1
        