class Num:
    def __init__(self, v: int):
        self.v = v
        self.valid = True


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.uniq = deque()
        self.resm = {}

        for n in nums:
            if n in self.resm:
                self.resm[n].valid = False
            else:
                self.add(n)


    def showFirstUnique(self) -> int:
        while self.uniq and not self.uniq[0].valid:
            self.uniq.popleft()

        return self.uniq[0].v if self.uniq else -1

    def add(self, n: int) -> None:
            if n in self.resm:
                self.resm[n].valid = False
            else:
                num = Num(n)
                self.resm[n] = num
                self.uniq.append(num)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
