class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            if i > len(s)-1:
                break
            if s[i] == c:
                i+=1
        if i == len(s):
            return True
        else:
            return False