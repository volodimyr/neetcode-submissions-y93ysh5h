class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        nums = defaultdict(int)

        for a in arr:
            nums[a] += 1
        
        res = 0
        for k, v in nums.items():
            if k+1 in nums:
                res += v
        
        return res
