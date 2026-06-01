class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        N = len(arr)
        first, last = arr[0], arr[N-1]
        prg = (last - first) // N
        if prg == 0:
            return arr[0]
        i = 1
        pred = arr[0] + prg
        while arr[i] == pred:
            pred = arr[i] + prg
            i += 1

        return pred

