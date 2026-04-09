class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = [0]*26
        for c in magazine:
            counter[ord(c) - ord('a')] += 1
        
        for c in ransomNote:
            if counter[ord(c) - ord('a')]-1 < 0:
                return False
            counter[ord(c) - ord('a')]-=1
        return True