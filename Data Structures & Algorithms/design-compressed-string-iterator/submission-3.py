class StringIterator:

    def __init__(self, compressedString: str):
        self.compressed = compressedString
        self.cur = 0
        self.cur_count = 0
        i = 1
        n = ''
        while i < len(self.compressed) and self.compressed[i].isdigit():
            n += self.compressed[i]
            i += 1
        if n:
            self.cur_count = int(n)

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        self.cur_count -= 1
        res = self.compressed[self.cur]

        if self.cur_count <= 0:

            self.cur += 1

            # next cur
            while self.cur < len(self.compressed) and self.compressed[self.cur].isdigit():
                self.cur += 1
            
            i = self.cur + 1
            n = ''
            while i < len(self.compressed) and self.compressed[i].isdigit():
                n += self.compressed[i]
                i += 1
            if n:
                self.cur_count = int(n)


        return res

    def hasNext(self) -> bool:
        return True if self.cur_count > 0 else False


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
