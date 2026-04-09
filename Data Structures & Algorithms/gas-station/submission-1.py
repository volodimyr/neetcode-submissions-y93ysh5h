class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        gas = gas + gas
        cost = cost + cost
        for L in range(N):
            R = L
            cur = 0
            while True:
                cur += gas[R]
                cur -= cost[R]
                if cur < 0:
                    L = R
                    break
                R+=1
                if R-L == N:
                    return L
        
        return -1

            