class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return True
        if len(s) != len(t):
            return False
        
        ms, mt = {}, {}
        for i in range(len(s)):
            if s[i] not in ms:
                ms[s[i]] = i
            if t[i] not in mt:
                mt[t[i]] = i
            
            if mt[t[i]] != ms[s[i]]:
                return False
        
        return True