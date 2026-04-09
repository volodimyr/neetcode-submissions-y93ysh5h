class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = (0, i)
            count, index = m[s[i]]
            count+=1
            m[s[i]] = (count, index)

        for c in s:
            if m[c][0] == 1:
                return m[c][1]


        return -1