class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for char in s[::-1]:
            if char == " ":
                if not count:
                    continue
                if count:
                    break
            count+=1
        return count
        