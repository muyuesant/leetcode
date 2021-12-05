# https://leetcode.com/problems/fruit-into-baskets/
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        size = len(fruits)
        left = 0
        res = 0
        picks = {}
        for i, fruit in enumerate(fruits):
            picks[fruit] = picks.get(fruit,0)+1
            while len(picks) > 2:
                picks[fruits[left]] -= 1
                if picks[fruits[left]] == 0 :
                    picks.pop(fruits[left])
                left += 1
            res = max(res, i-left+1)
        return res
                    
                
        