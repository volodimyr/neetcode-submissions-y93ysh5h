class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        n3, n2, n1 = 0, 1, 1
        for i in range(3, n+1, 1):
            n1, n2, n3 = (n3 + n2 + n1), n1, n2
        return n1