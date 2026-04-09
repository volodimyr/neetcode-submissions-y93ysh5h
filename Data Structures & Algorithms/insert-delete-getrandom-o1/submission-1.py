class RandomizedSet:

    def __init__(self):
        self.m = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.m:
            return False
        self.arr.append(val)
        self.m[val] = len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.m:
            return False
        idx = self.m[val]
        last = self.arr[len(self.arr)-1]
        self.arr[idx] = last
        self.m[last] = idx
        self.arr.pop()
        del self.m[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()