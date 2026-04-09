class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        mtp = []

        zeroes = 0
        for i in range(len(num1)-1, -1, -1):
            n1 = int(num1[i])
            row = []
            for _ in range(zeroes):
                row.append(0)
            zeroes+=1

            carry = 0
            for j in range(len(num2)-1, -1, -1):
                n2 = int(num2[j])
                if (n1 * n2) + carry < 10:
                    row.append((n1*n2)+carry)
                    carry = 0
                else:
                    m = (n1*n2) + carry
                    row.append(m % 10)
                    carry = m // 10
            if carry:
                row.append(carry)
            mtp.append(row[::-1])

        if len(mtp) == 1:
            return ''.join(map(str, mtp[0]))
        
        mtp = mtp[::-1]
        COLS = len(mtp[0])
        for r in range(len(mtp)):
            if len(mtp[r]) < COLS:
                nrow = [0]*(COLS-len(mtp[r]))
                for c in range(len(mtp[r])):
                    nrow.append(mtp[r][c])
                mtp[r] = nrow
        
        res = []
        carry = 0
        for c in range(len(mtp[0])-1, -1, -1):
            s = 0
            for r in range(len(mtp)):
                s += mtp[r][c]

            s+=carry
            if s < 10:
                res.append(s)
                carry = 0
            else:
                res.append(s%10)
                carry = s // 10
            
        if carry:
            res.append(carry)
            
        
        return ''.join(map(str, res[::-1]))
