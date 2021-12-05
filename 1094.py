# https://leetcode.com/problems/car-pooling/
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # trips.sort(key = lambda x : x[1])
        # print(trips)
        carMap = {}
        for t in trips:
#             people hop on
            if t[1] not in carMap:
                carMap[t[1]] = t[0]
            else:
                carMap[t[1]] += t[0]
            #             people hop off
            if t[2] not in carMap:
                carMap[t[2]] = -t[0]
            else:
                carMap[t[2]] -= t[0]
        keys = list(carMap.keys())
        keys.sort()
        print(keys)
        for key in keys:
            capacity -= carMap[key]
            if capacity < 0:
                return False
        return True