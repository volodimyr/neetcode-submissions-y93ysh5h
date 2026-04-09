class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = deque(a)
        b = deque(b)
        while len(b) < len(a):
            b.appendleft('0')
        while len(a) < len(b):
            a.appendleft('0')
        
        m = {
            '000': ('0', '0'),
            '010': ('1', '0'),
            '100': ('1', '0'),
            '001': ('1', '0'),
            '110': ('0', '1'),
            '111': ('1', '1'),
            '011': ('0', '1'),
            '101': ('0', '1')
        }

        carry = '0'
        for i in range(len(a)-1, -1, -1):
            a[i], carry = m[a[i] + b[i] + carry]
            

        if carry != '0':
            a.appendleft('1') 


        return ''.join(a)