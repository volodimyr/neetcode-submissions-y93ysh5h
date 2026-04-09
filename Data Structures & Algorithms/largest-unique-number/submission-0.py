class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        cc = Counter(nums)
        largest = -1
        for c,v in cc.items():
            if v == 1:
                largest = max(largest, c)
        return largest