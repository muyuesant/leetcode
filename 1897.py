class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        map = {}
        for word in words:
            for ch in word:
                if ch not in map:
                    map[ch] = 1
                else:
                    map[ch]+=1
        size = len(words)
        for v in map.values():
            if v % size != 0:
                return False
        return True