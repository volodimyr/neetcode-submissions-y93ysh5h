class Solution:
    def maxDepth(self, s: str) -> int:
        
        res = -math.inf
        depth = 0
        for c in s:
            if c == '(':
                depth += 1
            if c == ')':
                depth -= 1
            res = max(res, depth)
        return res