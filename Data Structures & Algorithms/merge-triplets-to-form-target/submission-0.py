class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def valid(i):
            if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                return True
            return False
        
        def equal(arr):
            if arr[0] == target[0] and arr[1] == target[1] and arr[2] == target[2]:
                return True
            return False
        

        f = None
        k = -1
        for i in range(len(triplets)):
            if valid(i):
                k = i
                f = triplets[i]
                break
        if not f:
            return False
        if equal(f):
            return True
        
        for i in range(k+1, len(triplets)):
            if not valid(i):
                continue
            row = triplets[i]

            f[0] = max(f[0], row[0])
            f[1] = max(f[1], row[1])
            f[2] = max(f[2], row[2])
            if equal(f):
                return True
        
        return False
        
        