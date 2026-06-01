class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        neg_heap = []

        balance = 0
        count = 0
        for t in transactions:
            balance += t
            count += 1
            if t < 0:
                heapq.heappush(neg_heap, t)
            
            if balance < 0:
                balance -= heapq.heappop(neg_heap)
                count -= 1
        
        return count