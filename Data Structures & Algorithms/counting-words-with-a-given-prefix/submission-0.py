class Node:
    def __init__(self):
        self.children = {}
        self.times = 1

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str, length: int):
        cur = self.root
        for i in range (length):
            if word[i] not in cur.children:
                cur.children[word[i]] = Node()
            else:
                cur.children[word[i]].times += 1
            cur = cur.children[word[i]]
    
    def prefix(self, pref: str) -> int:
        cur = self.root
        for char in pref:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.times

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for word in words:
            if len(word) >= len(pref):
                trie.insert(word, len(pref))
        return trie.prefix(pref)
