class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for char in s[::-1]:
            if char == " " and count:
                break
            elif char == " " and not count:
                continue
            count+=1
        return count
        