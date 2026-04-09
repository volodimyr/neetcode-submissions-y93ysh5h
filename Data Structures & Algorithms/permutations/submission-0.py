class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(used, cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            else:
                for n in nums:
                    if n not in used:
                        cur.append(n)
                        used.add(n)
                    else:
                        continue
                    backtrack(used, cur)
                    cur.pop()
                    used.remove(n)
        backtrack(set(), [])
        return res