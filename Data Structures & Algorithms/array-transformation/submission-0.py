class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            res = []
            res.append(arr[0])
            changed = False
            for i in range(1, len(arr)-1, 1):
                res.append(arr[i])
                if arr[i-1] > arr[i] < arr[i+1]:
                    changed = True
                    res[i] += 1
                elif arr[i-1] < arr[i] > arr[i+1]:
                    changed = True
                    res[i] -= 1
            
            res.append(arr[len(arr)-1])
            arr = res
            if not changed:
                break
        
        return arr