class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        res = []
        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for n in counter.keys():
                if counter[n] > 0:
                    cur.append(n)
                    counter[n]-=1
                    backtrack(cur)
                    counter[n]+=1
                    cur.pop()

        nums.sort()
        backtrack([])
        return list(res)