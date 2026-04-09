class Solution:
    def rotateTheBox(self, grid: List[List[str]]) -> List[List[str]]:
        for i in range(len(grid)):
            R = 0
            stones = 0
            while R < len(grid[i]):
                if grid[i][R] == '#':
                    grid[i][R] = '.'
                    R+=1
                    stones+=1
                elif grid[i][R] == '.':
                    R+=1
                else:
                    L = R-1
                    while stones:
                        grid[i][L] = '#'
                        stones-=1
                        L-=1
                    R+=1
            # if left
            L = R-1
            while stones:
                grid[i][L] = '#'
                stones-=1
                L-=1

        return [list(row) for row in zip(*grid[::-1])]
