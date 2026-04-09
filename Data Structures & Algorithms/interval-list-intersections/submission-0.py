class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(firstList)):
            s1, e1 = firstList[i][0], firstList[i][1]

            j = 0
            while j < len(secondList) and e1 >= secondList[j][0]:
                s2, e2 = secondList[j][0], secondList[j][1]
                start, end = max(s1,s2), min(e1, e2)
                if start <= end:
                    res.append([start,end])
                j+=1
        
        return res