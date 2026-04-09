class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 2:
            return 1
        prev = 0
        built = 0
        while prev + 1 + built <= n:
            prev += 1
            built += prev
        return prev
