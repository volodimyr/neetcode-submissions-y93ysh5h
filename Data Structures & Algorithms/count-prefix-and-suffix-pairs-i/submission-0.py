class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(0, len(words)-1, 1):
            for j in range(i+1, len(words), 1):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count+=1
        return count