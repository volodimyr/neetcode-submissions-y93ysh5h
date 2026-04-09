class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        for _, times in counter.items():
            while times != 0:
                if times == 1:
                    return -1
                if times % 3 == 0:
                    res += times // 3
                    break
                else:
                    res += 1
                    times -= 2
        
        return res