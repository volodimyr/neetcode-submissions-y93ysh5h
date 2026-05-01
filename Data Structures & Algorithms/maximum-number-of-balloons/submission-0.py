class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        res = 0
        while True:
            for c in 'balloon':
                if not counter[c]:
                    return res
                counter[c] -= 1
            res += 1
        