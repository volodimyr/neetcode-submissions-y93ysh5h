class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backt(i, cur):
            if i == len(nums):
                res.append(cur[:])
                return
            cur.append(nums[i])
            backt(i+1, cur)
            cur.pop()
            backt(i+1, cur)
        
        backt(0, [])
        return res