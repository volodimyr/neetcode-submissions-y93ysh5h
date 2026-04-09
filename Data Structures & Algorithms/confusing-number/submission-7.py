class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid = [2,3,4,5,7]
        m = {0:0, 1:1, 6: 9, 8:8, 9:6}
        res = 0
        orgn = n
        while n > 0:
            k = n % 10
            if k in invalid:
                return False
            k = m[k]
            res *= 10
            res += k
            n //= 10
        
        return res != orgn