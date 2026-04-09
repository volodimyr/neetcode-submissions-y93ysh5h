from sortedcontainers import SortedSet
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        if len(arr) < k:
            return ''
        res = SortedSet()
        dup = {}
        for i in range(len(arr)):
            s = arr[i]
            if s not in dup:
                dup[s] = i
                res.add((i, s))
            elif (dup[s], s) in res:
                res.remove((dup[s], s))
        if len(res) < k:
            return ''

        return res[k-1][1]