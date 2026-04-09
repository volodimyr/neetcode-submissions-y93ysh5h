class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        minheap = []
        if COLS != 1:
            heapq.heappush(minheap, (abs(heights[0][0] - heights[0][1]), 0, 1))
        if ROWS != 1:
            heapq.heappush(minheap, (abs(heights[0][0] - heights[1][0]), 1, 0))

        visit = set()
        while minheap:
            effort, i, j = heapq.heappop(minheap)
            if i == ROWS-1 and j == COLS-1:
                return effort
            if (i,j) in visit:
                continue
            visit.add((i,j))

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                i1, j1 = i+dr, j+dc
                if min(i1, j1) < 0:
                    continue
                if i1 == ROWS or j1 == COLS:
                    continue
                if (i1, j1) not in visit:
                    effort1 = abs(heights[i][j] - heights[i1][j1])
                    heapq.heappush(minheap, (max(effort, effort1), i1, j1))
        
        return 0
