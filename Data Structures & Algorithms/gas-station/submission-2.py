class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        N = len(gas)

        total = 0
        res = 0
        for i in range(N):
            total += gas[i]
            total -= cost[i]
            if total < 0:
                res = i+1
                total = 0

        return res

            