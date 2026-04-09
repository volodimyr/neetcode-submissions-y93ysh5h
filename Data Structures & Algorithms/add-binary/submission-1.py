class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = deque(a)
        b = deque(b)
        while len(b) < len(a):
            b.appendleft('0')
        while len(a) < len(b):
            a.appendleft('0')

        carry = '0'
        for i in range(len(a)-1, -1, -1):
            n = a[i] + b[i] + carry
            if n == '000':
                a[i] = '0'
            elif n == '010' or n == '100':
                a[i] = '1'
            elif n == '001':
                carry = '0'
                a[i] = '1'
            elif n == '111':
                a[i] = '1'
            else:
                carry = '1'
                a[i] = '0'
            

        if carry != '0':
            a.appendleft('1') 


        return ''.join(a)