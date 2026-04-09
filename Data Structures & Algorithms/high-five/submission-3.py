class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        sortm = {}
        for id, score in items:
            if id not in sortm:
                sortm[id] = []

            heapq.heappush(sortm[id], -score)
        
        res = []
        for usr, scores in sortm.items():
            summ = 0
            count = 0
            while scores and count < 5 :
                summ -= heapq.heappop(scores)
                count+=1
            
            res.append([usr, summ//5])

        return sorted(res)