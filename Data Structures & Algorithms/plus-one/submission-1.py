class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + 1 == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i]+=1
                break
            if i == 0 and carry == 1 and digits[i]+1 == 1:
                digits.insert(0, 1)
                return digits
            if i == 0 and carry == 1:
                digits[i]+=1
                
            
        return digits