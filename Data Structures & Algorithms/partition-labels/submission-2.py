class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        for i in range(len(s)):
            c = s[i]
            m[c] = i
        
        last_index = 0
        j = 0
        res = []
        for i in range(len(s)):
            j+=1
            c = s[i]
            last_index = max(last_index, m[c])

            if last_index == i:
                res.append(j)
                j = 0
        
        return res