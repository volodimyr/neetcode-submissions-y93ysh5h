class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in range (len(arr)):
            res.append(arr[i])
            if len(res) <= k:
                continue
            if res[0] == res[-1]:
                res.pop(0)
                continue
            first = abs(res[0]-x)
            last = abs(res[-1]-x)
            if first == last:
                res.pop()
                break
            if first < last:
                res.pop()
                break
            else:
                res.pop(0)

        return res