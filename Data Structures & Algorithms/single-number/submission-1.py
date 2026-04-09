class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for k, v in counter.items():
            if v == 1:
                return k
        return 0
        