class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, cur = set(), []
        find(0, nums, subsets, cur)
        return list(subsets)
    
def find(i, nums, subsets, cur):
    if i >= len(nums):
        subsets.add(tuple(cur.copy()))
        return
    cur.append(nums[i])
    find(i+1, nums, subsets, cur)
    cur.pop()
    find(i+1, nums, subsets, cur)