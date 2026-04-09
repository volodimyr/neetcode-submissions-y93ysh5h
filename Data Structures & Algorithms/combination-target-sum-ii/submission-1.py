class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(i, cur, total):
            if total == target:
                subsets.append(cur[:])
                return
            if total > target or i == len(candidates):
                return
            cur.append(candidates[i])
            backtrack(i+1, cur, total+candidates[i])
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1
            cur.pop()
            backtrack(i+1, cur, total)
        
        subsets = []
        backtrack(0, [], 0)

        return subsets
