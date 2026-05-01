class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        mn, mx = min(heights), max(heights)
        c = Counter(heights)

        ch = []
        for n in range(mn, mx+1):
            for _ in range(c[n]):
                ch.append(n)
        
        res = 0
        for i in range(len(ch)):
            if ch[i] != heights[i]:
                res += 1
        return res