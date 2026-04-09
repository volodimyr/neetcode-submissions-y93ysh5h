class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)

        odd, even = 0, math.inf
        for _, v in c.items():
            if v % 2 == 0:
                even = min(even, v)
            else:
                odd = max(odd, v)
        
        return odd - even