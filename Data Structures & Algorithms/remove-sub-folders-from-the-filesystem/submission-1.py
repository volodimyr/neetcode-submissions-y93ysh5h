from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.insert(f)
        
        return trie.to_list()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, folder: str):
        cur = self.root
        for f in folder[1:].split("/"):
            if f not in cur.ch:
                cur.ch[f] = TrieNode()
            cur = cur.ch[f]
        cur.folder = True
    
    def to_list(self) -> List[str]:
        res = []
        def dfs(cur, path):
            if cur.folder:
                res.append(path)
                return
            
            for name, tn in cur.ch.items():
                dfs(tn, path+"/"+name)

        dfs(self.root, "")
        return res


class TrieNode:
    def __init__(self):
        self.ch = {}
        self.folder = False
