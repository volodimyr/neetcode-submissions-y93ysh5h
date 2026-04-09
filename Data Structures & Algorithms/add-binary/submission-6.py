class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0

        i, j = len(a)-1, len(b)-1
        while i>=0 or j >=0 or carry > 0:
            da = int(a[i]) if i >= 0 else 0
            db = int(b[j]) if j >= 0 else 0

            total = da + db + carry
            carry = total // 2
            res.append(total % 2)

            i-=1
            j-=1

        res.reverse()
        return ''.join(map(str, res))