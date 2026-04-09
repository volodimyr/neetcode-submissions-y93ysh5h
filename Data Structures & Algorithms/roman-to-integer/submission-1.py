class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,

            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,

        }
        N = len(s)
        res = []
        L = 0
        R = 2
        while L < N:
            if R <= N and s[L:R] in m:
                res.append(m[s[L:R]])
                L = R
                R += 2
            else:
                ch = s[L]
                res.append(m[ch])
                L+=1
                R+=1

            
        return  sum(res)