class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        N = len(word)
        M = len(abbr)

        a, w = 0, 0

        while w < N and a < M:
            if '0' <= abbr[a] <= '9':
                nstr = ""
                while a < M and '0' <= abbr[a] <= '9':
                    nstr += abbr[a]
                    if nstr == '0':
                        return False
                    a+=1
                
                skip = int(nstr)
                for i in range(skip):
                    if w >= N:
                        return False
                    w+=1
            else:
                if abbr[a] != word[w]:
                    return False
                a+=1
                w+=1
        
        return w == N and a == M