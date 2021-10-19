class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        targetSum = threshold * k
        result = 0
        
        temp = 0
        for j in range(k):
            temp += arr[j]
        if temp > targetSum or temp == targetSum:
            result +=1    
        
            
        for i in range(1,len(arr)-k+1):
            # temp -= arr[i-1]
            temp += arr[i+k-1] - arr[i-1]
            
            if temp > targetSum or temp == targetSum:
                result +=1
        return result