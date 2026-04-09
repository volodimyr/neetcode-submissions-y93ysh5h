class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ex = set()
        mx = 1
        for n in nums:
            if n < 1:
                continue
            mx = max(mx, n)
            ex.add(n)
        
        for n in range(1, mx+2):
            if n not in ex:
                return n