class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        if N == 1:
            return 1
        res = 0
        def helper(L, R, res):
            while L >= 0 and R < N and s[L] == s[R]:
                res+=1
                R+=1
                L-=1
            return res
        
        for i in range(N):
            res = helper(i, i, res)
            res = helper(i, i+1, res)
        
        return res