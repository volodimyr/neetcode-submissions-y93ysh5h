class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = [0,0,0]

        for row in triplets:
            if row[0] <= target[0] and row[1] <= target[1] and row[2] <= target[2]:
                good[0] = max(row[0], good[0])
                good[1] = max(row[1], good[1])
                good[2] = max(row[2], good[2])

        return good == target
        
        