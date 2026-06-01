class StringIterator:

    def __init__(self, compressedString: str):
        self.uncompressed = ''
        for i in range(len(compressedString)):
            c = compressedString[i]
            if c.isdigit():
                n = c
                while i + 1 < len(compressedString) and compressedString[i + 1].isdigit():
                    i += 1
                    n += compressedString[i]
                n = int(n) 
                if n > 1:
                    self.uncompressed += self.uncompressed[-1] * (n - 1)
            elif not c.isdigit():
                self.uncompressed += c
        self.cur = 0

    def next(self) -> str:
        if self.cur >= len(self.uncompressed):
            return ' '
        c = self.uncompressed[self.cur]
        self.cur += 1
        return c

    def hasNext(self) -> bool:
        return True if self.cur < len(self.uncompressed) else False


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
