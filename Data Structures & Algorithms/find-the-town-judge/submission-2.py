class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count_trust = defaultdict(int)
        people = set()

        for p, t in trust:
            count_trust[t]+=1
            people.add(p)

        for i in range (1, n+1, 1):
            if i in people:
                continue
            trust_level = count_trust[i]
            if trust_level == n-1:
                return i

        return -1       
