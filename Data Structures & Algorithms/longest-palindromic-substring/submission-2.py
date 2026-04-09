class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        def helper(L, R):
            if L < 0 or R >= N:
                return ''
            
            paldr = ''
            while L >= 0 and R < N and s[L] == s[R]:
                paldr = s[L:R+1]
                L-=1
                R+=1
            return paldr

        mx = ''
        for i in range(N):
            odd = helper(i, i)
            if len(odd) > len(mx):
                mx = odd
            
            even = helper(i, i+1)
            if len(even) > len(mx):
                mx = even
        
        return mx
    