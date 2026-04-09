class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        n = len(arr)
        window = 0
        for i in range(k):
            window += arr[i]
        count = 0
        count += avg(window, k, threshold)
        
        for i in range(k, n, 1):
            window += arr[i]
            window -= arr[i-k]
            count += avg(window, k, threshold)

        return count

def avg(sum: int, k: int, threshold: int) -> int:
    if sum / k >= threshold:
        return 1
    return 0