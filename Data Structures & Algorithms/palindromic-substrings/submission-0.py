class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        if N == 1:
            return 1
        res = []
        def helper(L, R):
            while L >= 0 and R < N and s[L] == s[R]:
                res.append(s[L:R+1])
                R+=1
                L-=1
        
        for i in range(N):
            helper(i, i)
            helper(i, i+1)
        
        return len(res)