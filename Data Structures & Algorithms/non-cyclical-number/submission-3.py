class Solution:
    def isHappy(self, n: int) -> bool:
        sqsum = self.calc(n)
        res = set()
        while sqsum not in res:
            res.add(sqsum)
            if sqsum == 1:
                return True
            sqsum = self.calc(sqsum)
        return False

    def calc(self, n: int) -> int:
        sqsum = 0
        for char in str(n):
            sqsum += int(char) ** 2
        return sqsum