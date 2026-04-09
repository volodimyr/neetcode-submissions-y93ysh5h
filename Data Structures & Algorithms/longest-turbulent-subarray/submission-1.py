class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        same = arr[0]
        for i in range (1, len(arr)):
            if arr[i] != same:
                same = arr[i]
                break
        if same == arr[0]:
            return 1
        
        flips = [arr[0]]
        maxlen = 1
        for i in range (len(arr)-1):
            if flips[len(flips)-1] > arr[i]:
                if arr[i] < arr[i+1]:
                    flips.append(arr[i])
                    maxlen = max(maxlen, len(flips))
                else:
                    flips = [arr[i]]
            elif flips[len(flips)-1] < arr[i]:
                if arr[i] > arr[i+1]:
                    flips.append(arr[i])
                    maxlen = max(maxlen, len(flips))
                else:
                    flips = [arr[i]]
        return maxlen+1

