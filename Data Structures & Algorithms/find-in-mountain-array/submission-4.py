# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        L, R = 0, length - 1
        while L < R:
            m = L + (R - L) // 2
            if mountainArr.get(m) < mountainArr.get(m + 1):
                L = m + 1
            else:
                R = m
        peak = L
        
        peakv = mountainArr.get(peak)
        if peakv == target:
            return peak
        if peakv < target:
            return -1
        
        found = self.search(target, 0, peak-1, False, mountainArr)
        if found != -1:
            return found
        return self.search(target, peak + 1, length-1, True, mountainArr)
    
    def search(self, target, L, R, descending, mountainArr):
        while L <= R:
            m = L + (R-L) // 2
            mid = mountainArr.get(m)
            if target == mid:
                return m
            if descending:
                if target > mid:
                    R = m - 1
                else:
                    L = m + 1
            else:
                if target > mid:
                    L = m + 1
                else:
                    R = m - 1
        return -1
        