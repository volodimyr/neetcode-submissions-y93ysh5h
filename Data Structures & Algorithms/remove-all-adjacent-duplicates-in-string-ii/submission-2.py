class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        arr = []

        for c in s:
            if not arr:
                arr.append((c, 1))
            else:
                endc, count = arr[-1]
                if endc != c:
                    arr.append((c, 1))
                else:
                    if count + 1 == k:
                        arr.pop()
                    else:
                        arr[-1] = (c, count+1)
        
        return "".join(c * count for c, count in arr)