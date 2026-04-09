class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)

        arr = [0] * 26
        ln = 0
        res = []
        for c in s:
            ln += 1
            arr[ord(c)-97] += 1

            uniq = True
            for i in range(len(arr)):
                if arr[i] <= 0:
                    continue
                else:
                    cur = arr[i]
                    if counter[chr(i+97)] != arr[i]:
                        uniq = False
                        break
            if uniq:
                res.append(ln)
                ln = 0
                arr = [0] * 26
        
        return res


            
            
