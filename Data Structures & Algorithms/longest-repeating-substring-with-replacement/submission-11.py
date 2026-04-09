class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        max_len = 0
        for c in chars:
            count = L = 0
            for R in range (len(s)):
                if c == s[R]:
                    count+=1
                while R-L+1-count > k:
                    if c == s[L]:
                        count-=1
                    L+=1
                max_len = max(max_len, R-L+1)
        return max_len