# https://leetcode.com/problems/bulls-and-cows/
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sMap = {}
        gMap = {}
        for c in secret:
            if c not in sMap:
                sMap[c] = 1
            else:
                sMap[c] += 1
                
        for c in guess:
            if c not in gMap:
                gMap[c] = 1
            else:
                gMap[c] += 1
        # print(sMap)
        # print(gMap)
        
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                sMap[secret[i]] -= 1
                gMap[secret[i]] -= 1
                bulls += 1
        # print(sMap)
        # print(gMap)
        for k in gMap.keys():
            if k not in sMap:
                continue
            cows += min(sMap[k], gMap[k])
        
        # print(bulls, cows)
        return str(bulls)+"A"+str(cows)+"B"