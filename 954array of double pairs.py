# https://leetcode.com/problems/array-of-doubled-pairs/
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        numMap = {}
        zero = 0
        for n in arr:
            if n == 0:
                zero += 1
                continue
            if n in numMap:
                numMap[n] += 1
            else:
                numMap[n] = 1
        if zero % 2 != 0:
            return False
        keys = list(numMap.keys())
        keys.sort()
        pivit =0
        for i in range(len(keys)):
            if keys[i] < 0:
                pivit = i
            else:
                break
        if pivit < len(keys)-1:
            negKeys = list(reversed(keys[0:pivit+1]))
            keys = negKeys + keys[pivit+1:]
        else:
            keys = list(reversed(keys))
        # print(keys)
        
        while numMap:
            for i in keys:
                if i in numMap:
                    if i*2 in numMap:
                        temp = min(numMap[i], numMap[i*2])
                        numMap[i] -= temp
                        numMap[i*2] -= temp
                        if numMap[i] == 0:
                            numMap.pop(i)
                        if numMap[i*2] == 0:
                            numMap.pop(i*2)
                    else:
                        return False
        return True