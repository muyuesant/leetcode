class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        map1 = {}
        result = []
        arr1 = s1.split(" ")
        arr2 = s2.split(" ")
        for s in arr1:
            if s not in map1:
                map1[s] = 1
            else:
                map1[s] += 1
        for s in arr2:
            if s not in map1:
                map1[s] = 1
            else:
                map1[s] += 1
        for k , v in map1.items():
            if v == 1:
                result.append(k)
        return result