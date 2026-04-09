class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, cur = [], []
        find(0, nums, subsets, cur)
        return subsets
    
def find(i, nums, subsets, cur):
    if i >= len(nums):
        subsets.append(cur.copy())
        return
    cur.append(nums[i])
    find(i+1, nums, subsets, cur)
    cur.pop()
    find(i+1, nums, subsets, cur)