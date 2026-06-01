class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        horizontal = 0
        for c in range(self.n):
            if self.board[row][c] != player:
                break
            horizontal += 1
        if horizontal == self.n:
            return player
        
        vertical = 0
        for r in range(self.n):
            if self.board[r][col] != player:
                break
            vertical += 1
        if vertical == self.n:
            return player
        
        diagonal = 1
        # up
        r, c = row, col
        while True:
            r -= 1
            c -= 1
            if min(r, c) < 0:
                break
            if self.board[r][c] != player:
                break
            diagonal += 1
        
        # down
        r, c = row, col
        while True:
            r += 1
            c += 1
            if max(r, c) >= self.n:
                break
            if self.board[r][c] != player:
                break
            diagonal += 1
        

        if diagonal == self.n:
            return player


        diagonal = 1
        r, c = row, col
        while True:
            r -= 1
            c += 1
            if r < 0:
                break
            if c >= self.n:
                break
            if self.board[r][c] != player:
                break
            diagonal += 1
        
        # down
        r, c = row, col
        while True:
            r += 1
            c -= 1
            if c < 0:
                break
            if r >= self.n:
                break
            if self.board[r][c] != player:
                break
            diagonal += 1

        return player if diagonal == self.n else 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
