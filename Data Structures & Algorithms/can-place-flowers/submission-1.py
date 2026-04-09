class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while True:
            if n == 0:
                return True
            if i >= len(flowerbed):
                return False
            if flowerbed[i] == 1:
                pass                
            elif (i-1 < 0 or flowerbed[i-1] == 0) and (i+1 >= len(flowerbed) or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            i += 2


        return False
            