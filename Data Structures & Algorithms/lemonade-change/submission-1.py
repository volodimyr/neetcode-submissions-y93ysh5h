class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = deque(), deque()

        for b in bills:
            change = b - 5
            if b == 5:
                five.append(5)
            else:
                while ten and change > 0 and change - 10 >= 0:
                    change -= ten.popleft()
                while five and change > 0:
                    change -= five.popleft()
                if b == 10:
                    ten.append(10)
                
            if change > 0:
                return False

        return True