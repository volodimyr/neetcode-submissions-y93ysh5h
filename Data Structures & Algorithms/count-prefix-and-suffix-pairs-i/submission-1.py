class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word:str) -> None:
        cur = self.root
        for s, e in zip(word, reversed(word)):
            if (s, e) not in cur.children:
                cur.children[(s, e)] = TrieNode()
            cur = cur.children[(s,e)]
            cur.count+=1
    
    def count(self, word:str) -> int:
        cur = self.root
        for s, e in zip(word, reversed(word)):
            if (s, e) not in cur.children:
                return 0
            cur = cur.children[(s,e)]
        return cur.count
    

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        count = 0
        for word in words[::-1]:
            count += trie.count(word)
            trie.insert(word)
        return count
