# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def isCrossing(arr1: List[int], arr2: List[int]) -> List[int]:
            size1 = len(arr1)
            size2 = len(arr2)
            if arr1[0] < arr2[0] and arr2[0] < arr1[size1-1]:
                return [arr1[0], max(arr1[size1-1], arr2[size2-1])]
            elif arr2[0] < arr1[0] and arr1[0] < arr2[size2-1]:
                return [arr2[0], max(arr1[size1-1], arr2[size2-1])]
            else:
                return None
            
        charMap = {}
        for i in range(len(s)):
            if s[i] not in charMap:
                charMap[s[i]] = []
            charMap[s[i]].append(i)
        # print(charMap)
       
        values = list(charMap.values())
        tempResult = [values.pop(0)]
        # print(tempResult)
        for v in values:
            for i in range(len(tempResult)):
                crossed = False
                temp = isCrossing(v, tempResult[i])
                if temp is not None:
                    tempResult[i] = temp
                    crossed = True
                    break
            if not crossed:
                tempResult.append(v)
        # print(tempResult)
        result = []
        for t in tempResult:
            result.append(t[-1] - t[0] +1)
        # print(result)
        return result
                
            
            
            
            