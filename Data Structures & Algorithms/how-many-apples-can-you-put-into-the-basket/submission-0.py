class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()

        overall = 5000
        res = 0
        for w in weight:
            if overall - w >= 0:
                overall -= w
                res += 1
            else:
                break
        
        return res