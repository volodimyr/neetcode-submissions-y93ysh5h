class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = {}
        adj[beginWord] = []
        for i in range(len(wordList)):
            adj[wordList[i]] = []
            if self.has_edge(beginWord, wordList[i]):
                adj[beginWord].append(wordList[i])
                adj[wordList[i]].append(beginWord)
        
        for i in range(len(wordList)-1):
            for j in range(i+1, len(wordList)):
                if self.has_edge(wordList[i], wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        
        q = deque()
        visit = set()
        visit.add(beginWord)
        for dst in adj[beginWord]:
            visit.add(dst)
            q.append(dst)
        
        count = 0
        while q:
            count+=1
            for i in range(len(q)):
                pop = q.popleft()
                if pop == endWord:
                    return count+1
                for dst in adj[pop]:
                    if dst not in visit:
                        visit.add(dst)
                        q.append(dst)

                
        return 0
    
    def has_edge(self, g1: str, g2: str) -> bool:
        if g1 == g2:
            return False
        count = 0
        for i in range(len(g1)):
            if g1[i] != g2[i]:
                count+=1
            if count > 1:
                return False

        return True