class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        s.reverse()
        
        L, R = 0, 0
        while True:
            if R == len(s) or s[R].isspace():
                j = R-1
                while L < j:
                    s[L],s[j] = s[j],s[L]
                    L+=1
                    j-=1
                if R == len(s):
                    break
                L = R+1
                R += 1
            else:
                R+=1
