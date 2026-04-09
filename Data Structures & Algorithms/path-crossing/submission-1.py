class Solution:
    def isPathCrossing(self, path: str) -> bool:
        N = len(path)
        if N == 1:
            return False
        ps = set()
        ps.add((0, 0))
        i, j = 0, 0

        for dr in path:
            if dr == 'N':
                i += 1
            elif dr == 'S':
                i -= 1
            elif dr == 'W':
                j += 1
            else:
                j -= 1
            if (i,j) in ps:
                return True
            else:
                ps.add((i,j))

        return False