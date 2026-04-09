class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 0 and (i-1 < 0 or flowerbed[i-1] == 0) and (i+1 >= len(flowerbed) or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            i += 2


        return n == 0
            