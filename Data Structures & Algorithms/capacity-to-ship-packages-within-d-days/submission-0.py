class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)
        max_weight = max(weights)
        
        if days == 1:
            return total
        if days == len(weights):
            return max_weight
        
        left, right = max_weight, total
        min_capacity = 0
        
        while left <= right:
            mid = (left + right) // 2
            current_total = 0
            days_needed = 1
            
            for weight in weights:
                if current_total + weight > mid:
                    days_needed += 1
                    current_total = 0
                current_total += weight
            
            if days_needed <= days:
                min_capacity = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return min_capacity