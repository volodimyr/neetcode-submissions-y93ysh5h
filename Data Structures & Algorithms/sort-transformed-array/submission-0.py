class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = [0] * len(nums)
        L, R = 0, len(nums)-1

        index = 0 if a < 0 else len(nums)-1
        while L <= R:
            x1 = a*(nums[L]*nums[L]) + b*nums[L] + c
            x2 = a*(nums[R]*nums[R]) + b*nums[R] + c
            
            if a < 0:
                if x1 <= x2:
                    res[index] = x1
                    L += 1
                else:
                    res[index] = x2
                    R -= 1
                index += 1
            else:
                if x1 >= x2:
                    res[index] = x1
                    L += 1
                else:
                    res[index] = x2
                    R -= 1
                index -= 1



        return res