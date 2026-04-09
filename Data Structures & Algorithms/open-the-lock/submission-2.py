class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        q = deque([("0000", 0)])
        visit = set("0000")
        while q:
            lock, steps = q.popleft()
            if lock == target:
                return steps
            for i in range(4):
                digit = int(lock[i])
                for move in [1, -1]:
                    new_digit = (digit + move) % 10
                    new_char = str(new_digit)
                    nlock = lock[:i] + new_char + lock[i+1:]
                    if nlock not in visit and nlock not in dead:
                        q.append([nlock, steps + 1])
                        visit.add(nlock)
        return -1
