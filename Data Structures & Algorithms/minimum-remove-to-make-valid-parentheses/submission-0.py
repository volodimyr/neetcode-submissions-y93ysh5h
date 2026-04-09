class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    res.append(stack.pop())
                    res.append(i)
            else:
                res.append(i)
        
        res = sorted(res)

        res1 = ''
        for r in res:
            res1 += s[r]

        return res1