class Solution:
    def stoneGameIII(self, values: List[int]) -> str:
        n = len(values)
        dp = [float("-inf")] * (n+1)
        dp[n] = 0

        for i in range(n-1, -1, -1):

            score = 0
            for j in range(i, min(n, i+3)):
                score += values[j]
                dp[i] = max(dp[i], score - dp[j+1])

        score = dp[0]
        if score > 0:
            return "Alice"
        if score == 0:
            return "Tie"
        return "Bob"