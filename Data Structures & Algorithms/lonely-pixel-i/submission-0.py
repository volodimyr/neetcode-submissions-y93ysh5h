class Solution:
    def findLonelyPixel(self, p: List[List[str]]) -> int:
        rows = {}
        cols = {}

        ROWS, COLS = len(p), len(p[0])

        for r in range(ROWS):
            count = 0
            for c in range(COLS):
                if p[r][c] == 'B':
                    count+=1
                if count > 1:
                    break
            
            if count <= 1:
                rows[r] = True
            else:
                rows[r] = False
        
        for c in range(COLS):
            count = 0
            for r in range(ROWS):
                if p[r][c] == 'B':
                    count+=1
                if count > 1:
                    break
            
            if count <= 1:
                cols[c] = True
            else:
                cols[c] = False
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if p[r][c] == 'B' and rows[r] and cols[c]:
                    res +=1

        return res 