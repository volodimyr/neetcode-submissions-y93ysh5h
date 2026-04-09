class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        self.find(0, subsets, candidates, [],0, target)
        return subsets

    def find(self, i: int, subsets: List[List[int]], candidates: List[int], cur: List[int], total: int, target: int):
        if i == len(candidates) or total > target:
            return
        if total == target:
            subsets.append(cur[:])
            return
        cur.append(candidates[i])
        self.find(i, subsets, candidates, cur, total+candidates[i], target)
        cur.pop()
        self.find(i+1, subsets, candidates, cur, total, target)