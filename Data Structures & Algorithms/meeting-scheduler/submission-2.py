class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        N = len(slots1)
        M = len(slots2)

        slots1.sort()
        slots2.sort()

        i = 0
        j = 0
        while i < N and j < M:
            i1, j2 = slots1[i], slots2[j]
            s = max(i1[0], j2[0])
            e = min(i1[1], j2[1])
            if s <= e and e-s >= duration:
                return [s, s+duration]
            if i1[1] < j2[1]:
                i += 1
            else:
                j += 1

        return []