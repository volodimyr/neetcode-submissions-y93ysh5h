class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):        
        self.width = width
        self.height = height

        self.body = deque()
        self.body.append((0, 0))

        self.occupies = set()
        self.occupies.add((0, 0))

        self.food = deque(food)

        self.end_game = False
        self.score = 0

        self.drs = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}

    def move(self, direction: str) -> int:
        if self.end_game:
            return -1
        
        nhr, nhc = self.body[0][0]+self.drs[direction][0], self.body[0][1]+self.drs[direction][1]
        if min(nhr, nhc) < 0 or nhr >= self.height or nhc >= self.width:
            self.end_game = True
            return -1
        
        nhead = (nhr,nhc)
        
        if self.food and self.food[0] == [nhr,nhc]:
            self.food.popleft()
            self.score += 1
        else:
            tailr, tailc = self.body.pop()
            self.occupies.remove((tailr, tailc))

        if (nhr, nhc) in self.occupies:
            self.end_game = True
            return -1
        
        self.body.appendleft(nhead)
        self.occupies.add((nhr, nhc))
        
        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
