class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        km = {}
        for i in range(len(keyboard)):
            km[keyboard[i]] = i
        
        res = 0
        cur = 0
        for w in word:
            res += abs(cur - km[w])
            cur = km[w]
        
        return res