class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        changed = True
        while changed:
            res = []
            res.append(arr[0])
            changed = False
            for i in range(1, len(arr)-1, 1):
                val = arr[i]
                if arr[i-1] > arr[i] < arr[i+1]:
                    changed = True
                    val += 1
                elif arr[i-1] < arr[i] > arr[i+1]:
                    changed = True
                    val -= 1
                res.append(val)
                
            res.append(arr[len(arr)-1])
            arr = res

        
        return arr