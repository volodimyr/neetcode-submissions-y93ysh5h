class WordDistance:

    def __init__(self, wordsDict: List[str]):
        N = len(wordsDict)
        self.m = {}
        for i in range(N):
            word = wordsDict[i]
            if word in self.m:
                self.m[word].append(i)
            else:
                self.m[word] = [i]
            


    def shortest(self, word1: str, word2: str) -> int:
        i1, i2 = 0, 0
        words1 = self.m[word1]
        words2 = self.m[word2]

        res = math.inf
        while i1 < len(words1) and i2 < len(words2):
            res = min(res, abs(words1[i1]-words2[i2]))
            if res == 1:
                break
            if words1[i1] < words2[i2]:
                i1 += 1
            else:
                i2 += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
