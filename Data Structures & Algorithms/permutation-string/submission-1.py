class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target  = [0]*26
        for c in s1:
            target[ord(c) - ord('a')]+=1

        s2count = [0]*26
        k = len(s1)
        for i in range (len(s2)):
            s2count[ord(s2[i]) - ord('a')]+=1
            if i+1 < k:
                continue
            if i+1 > k:
                s2count[ord(s2[i-k]) - ord('a')]-=1
            if target == s2count:
                return True
        
        return False