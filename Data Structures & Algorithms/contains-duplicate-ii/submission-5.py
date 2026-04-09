
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index = {}
        for i, n in enumerate(nums):
            if n in last_index and abs(i - last_index[n]) <= k:
                return True
            last_index[n] = i
        return False