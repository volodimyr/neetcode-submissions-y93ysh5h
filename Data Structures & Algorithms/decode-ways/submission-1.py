class Solution:
    def numDecodings(self, s: str) -> int:
        m = {str(i): chr(ord('A') + i - 1) for i in range(1, 27)}

        
        res = set()
        def dfs(i, arr):
            if i >= len(s):
                res.add(''.join(arr[:]))
                return
            if s[i] not in m:
                return
            arr.append(m[s[i]])
            dfs(i+1, arr)
            arr.pop()
            
            if i+1 <= len(s) and s[i:i+2] in m:
                arr.append(m[s[i:i+2]])
                dfs(i+2, arr)
        
        dfs(0, [])

        return len(res)