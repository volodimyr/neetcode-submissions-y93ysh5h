class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.sets = set()
        for i in range(maxNumbers):
            self.sets.add(i)
            

    def get(self) -> int:
        if not self.sets:
            return -1
        return self.sets.pop()

    def check(self, number: int) -> bool:
        return number in self.sets

    def release(self, number: int) -> None:
        self.sets.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
