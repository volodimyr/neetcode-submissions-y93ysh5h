class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tarr = [0] * 58
        for ts in t:
            try:
                tarr[ord(ts)-ord('A')] += 1
            except IndexError:
                return ord(ts)-ord('A')

        sarr = [0] * 58
        L, R = 0, 0
        res = ""
        while R < len(s):
            if not self.validate(tarr, sarr):
                sarr[ord(s[R]) - ord('A')] += 1
                R+=1
            else:
                if res == "" or len(res) > R-L:
                    res = s[L:R]
                sarr[ord(s[L]) - ord('A')] -= 1
                L+=1
                if len(res) == len(t):
                    return res
        
        while L < len(s) and self.validate(tarr, sarr):
            if res == "" or len(res) > R-L:
                res = s[L:R]
            sarr[ord(s[L]) - ord('A')] -= 1
            L+=1
            if len(res) == len(t):
                return res

        return res

    
    def validate(self, tarr, sarr):
        for i in range(len(tarr)):
            if tarr[i] > sarr[i]:
                return False
        return True