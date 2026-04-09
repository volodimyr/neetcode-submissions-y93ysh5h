class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        minheap = [(grid[0][0], 0, 0)]
        visit = set()
        while minheap:
            elev, i, j = heapq.heappop(minheap)
            if i == ROWS-1 and j == COLS-1:
                return elev
            if (i,j) in visit:
                continue
            visit.add((i,j))

            for dr, dc in [(1, 0), (-1,0), (0, 1), (0, -1)]:
                i1, j1 = dr+i, dc+j
                if min(i1, j1) < 0:
                    continue
                if i1 == ROWS or j1 == COLS:
                    continue
                heapq.heappush(minheap, (max(elev, grid[i1][j1]), i1, j1))
        return 0