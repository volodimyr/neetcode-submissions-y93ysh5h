class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ch = heights[:]
        ch.sort()
        res = 0
        for i in range(len(heights)):
            hi, chi = heights[i], ch[i]
            if hi != chi:
                res += 1
        
        return res