class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.sumup = 0
        self.max_size = size
        

    def next(self, val: int) -> float:
        if self.max_size == len(self.q):
            self.sumup -= self.q.popleft()
        self.sumup += val
        self.q.append(val)
        return self.sumup / len(self.q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
