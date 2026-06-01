class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        # self.maxN = maxNumbers
        # self.available = maxNumbers
        self.arr = [-1] * maxNumbers
        for i in range(maxNumbers):
            self.arr[i] = i
        self.pointer = 0
        self.N = maxNumbers
            

    def get(self) -> int:
        if self.pointer >= self.N:
            return -1
        n = self.arr[self.pointer]
        self.arr[self.pointer] = -1
        while self.pointer < self.N and self.arr[self.pointer] == -1:
            self.pointer += 1

        return n

    def check(self, number: int) -> bool:
        return True if number >= self.pointer else False

    def release(self, number: int) -> None:
        self.arr[number] = number
        if number < self.pointer or self.pointer == self.N or self.arr[self.pointer] == -1:
            self.pointer = number


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
