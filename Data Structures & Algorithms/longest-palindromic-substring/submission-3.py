class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        def helper(L, R):
            if L < 0 or R >= N:
                return ''            
            while L >= 0 and R < N and s[L] == s[R]:
                L-=1
                R+=1
            return s[L+1:R]

        mx = ''
        for i in range(N):
            odd = helper(i, i)
            if len(odd) > len(mx):
                mx = odd
            
            even = helper(i, i+1)
            if len(even) > len(mx):
                mx = even
            if len(mx) == N:
                break
        
        return mx