class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0

        for b in bills:
            change = b - 5
            if b == 5:
                five+=1
            if b == 10:
                ten+=1
            
            while ten and change > 0 and change - 10 >= 0:
                change -= 10
                ten -= 1

            while five and change > 0:
                change -= 5
                five -= 1

            if change > 0:
                return False

        return True