class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.calc(n)
        while slow != fast:
            fast = self.calc(fast)
            fast = self.calc(fast)
            slow = self.calc(slow)

        return True if slow == 1 else False

    def calc(self, n: int) -> int:
        out = 0
        while n:
            out += (n % 10) ** 2
            n //= 10
        return out