class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return 0
        org = x
        x = abs(x)
        res = 0
        while x:
            nexxt = x % 10
            res = res * 10 + nexxt
            x //= 10
        if org < 0:
            res *= -1
        if res < -(2**31) or res > (2**31-1):
            return 0
        return res