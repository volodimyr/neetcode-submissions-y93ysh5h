class Solution:
    def makesquare(self, ms: List[int]) -> bool:
        summ = sum(ms)
        if summ % 4 != 0:
            return False
        N = len(ms)

        ms.sort(reverse=True)
        sides = [0] * 4
        len_side = summ / 4

        def dfs(i):
            if i == N:
                return True
            
            for j in range(len(sides)):
                if sides[j] + ms[i] <= len_side:
                    sides[j] += ms[i] 
                    if dfs(i+1):
                        return True
                    sides[j] -= ms[i]

                if sides[j] == 0:
                    break

            return False
        
        return dfs(0)
                    