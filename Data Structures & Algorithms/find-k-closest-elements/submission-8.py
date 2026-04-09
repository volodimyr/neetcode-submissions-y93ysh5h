class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        window = deque()
        for num in arr:
            window.append(num)
            if len(window) > k:
                if window[0] == window[-1]:
                    window.popleft()
                    continue
                if abs(window[0] - x) > abs(window[-1] - x):
                    window.popleft()
                else:
                    window.pop()
                    break
        return list(window)