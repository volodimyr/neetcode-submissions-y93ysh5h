class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        cur = minutes-1
        totalnotgrumpy=0
        window = 0
        while cur >= 0:
            if grumpy[cur] == 0:
                totalnotgrumpy+=customers[cur]
            if grumpy[cur]==1:
                window += customers[cur]
            cur-=1
        maxresult = window

        for i in range(minutes, len(customers), 1):
            if grumpy[i]==0:
                totalnotgrumpy+=customers[i]
            if grumpy[i]==1:
                window+=customers[i]
            if grumpy[i-minutes]==1:
                window-=customers[i-minutes]
            maxresult = max(maxresult, window)
        return totalnotgrumpy+maxresult
