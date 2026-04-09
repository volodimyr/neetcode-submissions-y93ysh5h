class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        L, R = 0, len(nums) - 1
        
        while L <= R:
            L, R = self.skip_duplicates(nums, L, R)
            
            if L > R:
                break
                
            m = (L + R) // 2
            
            if target == nums[m]:
                return True
            if nums[L] <= nums[m]:
                if nums[L] <= target < nums[m]:
                    R = m - 1
                else:
                    L = m + 1
            else:
                if nums[m] < target <= nums[R]:
                    L = m + 1
                else:
                    R = m - 1
        
        return False
    
    def skip_duplicates(self, nums: List[int], L: int, R: int) -> tuple:
        while L < R:
            if L + 1 <= R and nums[L] == nums[L + 1]:
                L += 1
                continue            
            if R - 1 >= L and nums[R] == nums[R - 1]:
                R -= 1
                continue
            if nums[R] == nums[L]:
                R -= 1
                continue
            
            break
        
        return L, R
