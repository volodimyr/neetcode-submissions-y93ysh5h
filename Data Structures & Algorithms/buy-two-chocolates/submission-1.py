class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1, min2 = 1e9, 1e9
        for p in prices:
            if p < min1:
                min1, min2 = p, min1
            elif p < min2:
                min2 = p
        
        return money if money-min1-min2 < 0 else money-min1-min2