class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0 : 1}
        cur_sum = count = 0

        for n in nums:
            cur_sum+=n
            diff = cur_sum-k
            count += prefix.get(diff, 0)
            prefix[cur_sum] = 1 + prefix.get(cur_sum, 0)

        return count