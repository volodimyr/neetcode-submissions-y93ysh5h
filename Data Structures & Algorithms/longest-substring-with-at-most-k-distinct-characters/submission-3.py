class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        L = R = 0
        chars = defaultdict(int)
        res = 0
        while R < len(s):
            chars[s[R]]+=1
            while len(chars) > k:
                chars[s[L]]-=1
                if chars[s[L]] == 0:
                    del chars[s[L]]
                L+=1
            R+=1
            res = max(res, R-L)
        return res