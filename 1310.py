
# https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        size = len(arr)
        result = []
        
        for i in range(1,size):
            arr[i] ^= arr[i-1]
        
        for q in queries:
            if q[0] == 0:
                result.append(arr[q[1]])
            else:
                result.append(arr[q[0] - 1] ^ arr[q[1]])
        return result
       