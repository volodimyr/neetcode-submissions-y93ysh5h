class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [0] * (2 * l)
        for i, v in enumerate(nums):
            ans[i] = v
            ans[i + l] = v
        return ans