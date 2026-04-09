class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        for i in range(N):
            cur = 0
            j = i
            while True:
                cur += gas[j]
                cur -= cost[j]
                if cur < 0:
                    break
                
                j += 1
                if j == N:
                    j = 0
                if j == i:
                    return i
        
        return -1