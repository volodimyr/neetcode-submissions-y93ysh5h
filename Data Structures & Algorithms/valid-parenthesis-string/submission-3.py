class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        asterix = []

        for i in range(len(s)):
            ch = s[i]
            if ch == '(':
                stack.append(i)
            elif ch == '*':
                asterix.append(i)
            else:
                if stack:
                    stack.pop()
                elif not asterix:
                    return False
                else:
                    asterix.pop()
        
        while stack:
            if not asterix:
                return False
            if asterix[-1] < stack[-1]:
                return False
            stack.pop()
            asterix.pop()
        
        return True
        
