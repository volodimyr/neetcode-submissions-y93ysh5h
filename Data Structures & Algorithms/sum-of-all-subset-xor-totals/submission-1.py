class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = [0]
        def find(i, cur):
            if i >= len(nums):
                xor = 0
                for c in cur:
                    xor ^= c
                result[0] += xor
                return
            cur.append(nums[i])
            find(i+1, cur)
            cur.pop()
            find(i+1, cur)
        find(0, [])

        return result[0]