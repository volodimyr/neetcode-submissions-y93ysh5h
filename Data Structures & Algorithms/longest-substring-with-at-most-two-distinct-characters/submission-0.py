class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)
        letters = {}
        L = R = 0
        max_len = 0
        for c in s:
            R+=1
            letters[c] = letters.get(c, 0)+1
            while len(letters) > 2:
                count = letters[s[L]]
                if count > 1:
                    letters[s[L]] = count-1
                else:
                    del letters[s[L]]
                L+=1
            max_len = max(max_len, R-L)
        
        return max_len


