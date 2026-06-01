class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):        
        self.width = width
        self.height = height

        self.body = deque()
        self.body.append((0, 0))

        self.occupies = set()
        self.occupies.add((0, 0))

        self.food = deque(food)

        self.game_over = False
        self.score = 0

        self.drs = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}

    def move(self, direction: str) -> int:
        if self.game_over:
            return -1
        
        hr, hc = self.body[0]
        dr, dc = self.drs[direction]
        nhr, nhc = hr+dr, hc+dc
        if min(nhr, nhc) < 0 or nhr >= self.height or nhc >= self.width:
            self.game_over = True
            return -1
        
        nhead = (nhr,nhc)
        
        if self.food and tuple(self.food[0]) == nhead:
            self.food.popleft()
            self.score += 1
        else:
            tailr, tailc = self.body.pop()
            self.occupies.remove((tailr, tailc))

        if nhead in self.occupies:
            self.game_over = True
            return -1
        
        self.body.appendleft(nhead)
        self.occupies.add(nhead)
        
        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
