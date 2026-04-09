class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        def backtrack(cur, used):
            if len(cur) == len(nums):
                res.add(tuple(cur.copy()))
                return
            else:
                for i in range(len(nums)):
                    if (i, nums[i]) not in used:
                        cur.append(nums[i])
                        used.add((i, nums[i]))
                    else:
                        continue
                    backtrack(cur, used)
                    cur.pop()
                    used.remove((i, nums[i]))
        backtrack([], set())
        return list(res)