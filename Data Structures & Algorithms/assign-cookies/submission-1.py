class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0
        g.sort()
        s.sort()

        j = 0
        res = 0
        for i in range(len(g)):
            while j < len(s) and s[j] < g[i]:
                j += 1

            if j == len(s):
                break
            res += 1
            j += 1
            
        return res