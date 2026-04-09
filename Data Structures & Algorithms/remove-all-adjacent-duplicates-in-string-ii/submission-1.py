class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        arr = []

        for c in s:
            if not arr:
                arr.append((c,1))
            else:
                endc, count = arr[-1]
                if endc != c:
                    arr.append((c,1))
                else:
                    if count + 1 == k:
                        arr = arr[:-k+1]
                    else:
                        arr.append((c, count+1))
        
        return "".join(c for c,_ in arr)
        