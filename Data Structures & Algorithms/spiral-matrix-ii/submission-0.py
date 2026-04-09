class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visit = set()
        N = n*n
        arr = [[0 for _ in range(n)] for _ in range(n)] 
        
        q = deque()
        q.append((0,0))
        
        dr = 0
        val = 1
        while q:
            lastr, lastc = 0, 0
            for _ in range(len(q)):
                r, c = q.popleft()
                arr[r][c] = val
                val += 1
                visit.add((r,c))
                lastr, lastc = r, c
            
            while True:
                nr, nc = lastr+directions[dr][0], lastc+directions[dr][1]
                if (nr, nc) in visit:
                    break
                if min(nr, nc) < 0:
                    break
                if max(nr, nc) >= n:
                    break
                q.append((nr, nc))
                lastr, lastc = nr, nc
                
            dr += 1
            if dr > 3:
                dr = 0
        
        return arr