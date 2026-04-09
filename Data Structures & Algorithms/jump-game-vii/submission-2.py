class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        N = len(s)
        def reachable(i, j):
            if i + minJump <= j <=  min(i + maxJump, N-1) and s[j] == '0':
                return True
            else:
                return False
        
        q = deque()
        q.append(0)

        visit = set()
        visit.add(0)
        while q:
            for _ in range(len(q)):
                i = q.popleft()

                maxj = -math.inf
                minj = math.inf
                for j in range(i+1, N, 1):
                    if j in visit:
                        continue
                    if not reachable(i, j):
                        continue
                    if j == N-1:
                        return True
                    visit.add(j)
                    maxj = max(maxj, j)
                    minj = min(minj, j)
                if maxj != -math.inf:
                    q.append(maxj)
                if minj != math.inf:
                    q.append(minj)
        
        return False
                    
