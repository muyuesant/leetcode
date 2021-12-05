# https://leetcode.com/problems/find-original-array-from-doubled-array/
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # print(changed)
        size = len(changed)
        if size % 2 != 0:
            return []
        odds = {}
        evens = {}
        for i in changed:
            if i % 2 != 0:
                if i not in odds:
                    odds[i] = 1
                else:
                    odds[i] += 1
            else:
                if i not in evens:
                    evens[i] = 1
                else:
                    evens[i] += 1
        # print(odds)
        # print(evens)
        result = []
        
        oddKeys = list(odds.keys())
        for i in oddKeys:
            if i*2 in evens:
                if odds[i] > evens[i*2]:
                    return []
                
                evens[i*2] -= odds[i]
                result.extend([i for j in range(odds[i])])
                # odds.pop(i)
                if evens[i*2] == 0:
                    evens.pop(i*2)
            else:
                return []
            
        # if len(odds) > 0:
        #     return []
        
        
        if 0 in evens:
            if evens[0] % 2 == 0:
                result.extend([0 for i in range(evens[0]//2)])
                evens.pop(0)
            else:
                return []
        # print()
        # print(odds)
        # print(evens)  
        # print(result)
        
        evensKey = list(evens.keys())
        evensKey.sort()
        for i in evensKey:
            if i in evens and i*2 in evens:
                if evens[i] > evens[i*2]:
                    return []
                result.extend([i for j in range(evens[i])])
                evens[i*2] -= evens[i]
                evens.pop(i)
                if evens[i*2] == 0:
                    evens.pop(i*2)
        
        
       
        if len(evens) > 0:
            return []
                
            
        return result
        
        
        
        