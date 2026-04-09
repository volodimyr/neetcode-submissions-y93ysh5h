class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        subsets = []
        self.find(1, subsets, [], n, k)
        return subsets
        
    def find(self, i, subsets, cur, n, k: int):
        if len(cur) == k:
            subsets.append(cur.copy())
            return
        if i > n:
            return
        cur.append(i)
        self.find(i+1, subsets, cur, n, k)
        cur.pop()
        self.find(i+1, subsets, cur, n, k)


