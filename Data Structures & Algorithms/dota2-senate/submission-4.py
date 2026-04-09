class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)
    
        while r and d:
            ri = r.popleft()
            di = d.popleft()
            if ri < di:
                r.append(ri+len(senate))
            else:
                d.append(di+len(senate))
        
        return "Radiant" if r else 'Dire'