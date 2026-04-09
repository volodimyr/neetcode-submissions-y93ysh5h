class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        L, R = 0, length-1

        peak = 0
        while L <= R:
            m = L + (R-L) // 2
            mid = mountainArr.get(m)
            midl = mountainArr.get(m-1)
            midr = mountainArr.get(m+1)
            if mid > midl and mid > midr:
                peak = m
                break
            if mid < midr:
                L = m + 1
            else:
                R = m - 1
        
        peakv = mountainArr.get(peak)
        if peakv == target:
            return peak
        if peakv < target:
            return -1
        
        found = self.search(target, 0, peak-1, False, mountainArr)
        if found != -1:
            return found
        return self.search(target, peak + 1, length-1, True, mountainArr)
    
    def search(self, target, L, R, growing, mountainArr):
        while L <= R:
            m = L + (R-L) // 2
            mid = mountainArr.get(m)
            if target == mid:
                return m
            if growing:
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