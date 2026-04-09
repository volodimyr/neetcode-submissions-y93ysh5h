class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)
        memo = {}
        def dfs(i, o):
            if o < 0:
                return False
            if i == N:
                return o == 0
            if (i,o) in memo:
                return memo[(i, o)]
            ch = s[i]
            if ch == '(':
                memo[(i,o)] = dfs(i+1, o+1)
            elif ch == ')':
                memo[(i,o)] = dfs(i+1, o-1)
            else: 
                memo[(i,o)] = (dfs(i+1, o) or dfs(i+1, o+1) or dfs(i+1, o-1))

            return memo[(i,o)]
        
        return dfs(0, 0)