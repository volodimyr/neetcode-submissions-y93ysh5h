class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        m = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        res = ''
        for n in num:
            if n not in m:
                return False
            res += m[n]
        
        return res[::-1] == num