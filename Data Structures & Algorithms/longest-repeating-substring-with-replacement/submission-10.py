class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        max_count = 0
        L = 0
        max_len = 0

        for R in range(len(s)):
            idx = ord(s[R]) - ord('A')
            count[idx] += 1
            max_count = max(max_count, count[idx])
            while (R - L + 1) - max_count > k:
                count[ord(s[L]) - ord('A')] -= 1
                L += 1

            max_len = max(max_len, R - L + 1)

        return max_len