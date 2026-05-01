class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        lastw1, lastw2 = math.inf, math.inf
        res = math.inf
        for i in range(len(wordsDict)):
            word = wordsDict[i]
            if word == word1:
                lastw1 = i
            elif word == word2:
                lastw2 = i
                
            res = min(res, abs(lastw2-lastw1))
        
        return res
                