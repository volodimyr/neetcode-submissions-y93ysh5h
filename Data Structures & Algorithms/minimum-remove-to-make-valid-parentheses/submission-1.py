class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        persist = set()
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack.append(i)
            elif c == ')' and stack:
                persist.add(stack.pop())
                persist.add(i)
        
        res = []
        for i in range(len(s)):
            c = s[i]
            if (c == ')' or c == '('):
                if i in persist:
                    res.append(c)
            else:
                res.append(c)
            
        
        return ''.join(res)