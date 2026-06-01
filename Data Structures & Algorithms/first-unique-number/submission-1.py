
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque()
        self.unique = defaultdict(int)
        for n in nums:
            self.add(n)


    def showFirstUnique(self) -> int:
        while self.q and self.unique[self.q[0]] > 1:
            self.q.popleft()

        return self.q[0] if self.q else -1

    def add(self, n: int) -> None:
        self.unique[n] += 1
        self.q.append(n)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
