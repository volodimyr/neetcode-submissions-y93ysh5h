class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        zp = ''.join(words)
        for char in zp:
            if char not in adj:
                adj[char] = []

        for i in range(len(words)-1):
            prev, nxt = words[i], words[i+1]
            N = min(len(prev), len(nxt))
            diff = False
            index = 0
            for j in range(N):
                if prev[j] != nxt[j]:
                    diff = True
                    index = j
                    break
            if not diff:
                if len(prev) > len(nxt):
                    return ""
                continue
            adj[prev[index]].append(nxt[index])

        indegree = {char: 0 for char in adj}


        for k in adj:
            for v in adj[k]:
                indegree[v]+=1
    
        
        q = deque()
        for char, d in indegree.items():
            if d == 0:
                q.append(char)

        res = []
        while q:
            pop = q.popleft()
            res.append(pop)
            for node in adj[pop]:
                indegree[node]-=1
                if indegree[node] == 0:
                    q.append(node)
        
        if len(res) < len(adj):
            return ""
            
        return ''.join(res)
        
            
                