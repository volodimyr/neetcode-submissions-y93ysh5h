class Solution:
    def insert(self, intervals: List[List[int]], ni: List[int]) -> List[List[int]]:
        res = []
        new_interval_added = False
        for i in range(len(intervals)):
            if self.overlapped(ni, intervals[i]):
                ni = self.merge(ni, intervals[i])
                continue

            if ni[1] < intervals[i][0]:
                if not new_interval_added:
                    res.append(ni)
                new_interval_added = True
                res.append(intervals[i])
            else:
                res.append(intervals[i])

            
        if not new_interval_added:
            res.append(ni)
        
        return res
    
    def overlapped(self, n1, n2):
        if n1[0] >= n2[0] and n1[0] <= n2[1]:
            return True
        if n1[1] >= n2[0] and n1[1] <= n2[1]:
            return True
        if n1[0] <= n2[0] and n1[1] >= n2[1]:
            return True

        return False
    
    def merge(self, i1, i2):
        merged = []
        if i1[0] < i2[0]:
            merged.append(i1[0])
        else:
            merged.append(i2[0])
        
        if i1[1] < i2[1]:
            merged.append(i2[1])
        else:
            merged.append(i1[1])
        
        return merged