class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.ch:
                cur.ch[c] = Node()
            cur = cur.ch[c]
        cur.word = True
    
    def search(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.ch:
                return False
            cur = cur.ch[c]
        return cur.word

class Node:
    def __init__(self):
        self.ch = {}
        self.word = False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for w in wordDict:
            trie.insert(w)
        
        N = len(s)
        memo = {}
        def dfs(i, j, size):
            if j >= N+1:
                if size == N:
                    return True
                return False
            if (i, j, size) in memo:
                return memo[(i,j,size)]

            found = trie.search(s[i:j])
            skip = dfs(i, j+1, size)
            if not found:
                memo[(i,j,size)] = skip
                return skip

            res = skip or dfs(j, j+1, size+(j-i))
            memo[(i,j,size)] = res
            return res
        
        return dfs(0, 1, 0)

