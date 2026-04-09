class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        replace = arr[len(arr)-1]
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr)-1:
                arr[i] = -1
                continue
            last = arr[i]
            if last > replace:
                arr[i], replace = replace, last
            else:
                arr[i] = replace
        return arr