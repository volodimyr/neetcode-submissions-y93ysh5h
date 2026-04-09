class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        while True:
            first = heapq.heappop(sticks)
            if not sticks:
                break
            second = heapq.heappop(sticks)
            third = first + second
            heapq.heappush(sticks, third)
            res += third
        return res