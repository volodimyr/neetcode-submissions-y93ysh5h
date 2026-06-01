class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        counter = {}
        
        for i in range(k):
            c = s[i]
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1
        
        res = 0
        if len(counter) == k:
                res += 1
        for i in range(k, len(s)):
            forw = s[i]
            back = s[i-k]
            counter[back] -= 1
            if counter[back] == 0:
                del counter[back]
            if forw in counter:
                counter[forw] += 1
            else:
                counter[forw] = 1
            
            if len(counter) == k:
                res += 1
        
        return res
        
        