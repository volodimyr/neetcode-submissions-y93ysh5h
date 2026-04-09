class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        sortm = {}
        for id, score in items:
            if id not in sortm:
                sortm[id] = []

            heapq.heappush(sortm[id], -score)
        
        res = []
        for usr, scores in sortm.items():
            sum = 0
            count = 0
            while scores and count < 5 :
                sum -= heapq.heappop(scores)
                count+=1
            
            heapq.heappush(res, [usr, int(sum/5)])

        return res