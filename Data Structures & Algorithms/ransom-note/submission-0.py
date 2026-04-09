class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = Counter(magazine)
        for c in ransomNote:
            if c not in m:
                return False
            if m[c]-1 < 0:
                return False
            m[c]-=1
        return True