class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        visit = set()
        q = deque()
        q.append((0,0,0))
        visit.add((0,0))


        while q:
            x1, y1, moves = q.popleft()
            if x1 == x and y1 == y:
                return moves

            for dr, dc in ((-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)):
                nr, nc = x1+dr, y1+dc
                if nr < -2 or nc < -2:
                    continue
                if (nr,nc) in visit:
                    continue
                visit.add((nr,nc))
                q.append((nr,nc,moves+1))

        return -1