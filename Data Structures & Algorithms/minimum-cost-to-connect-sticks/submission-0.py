class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        h = []
        for s in sticks:
            heapq.heappush(h, s)

        res = 0
        while True:
            first = heapq.heappop(h)
            if not h:
                return res
            second = heapq.heappop(h)
            third = first + second
            heapq.heappush(h, third)
            res += third
