class TreeNode:
    def __init__(self):
        self.children = {}
        self.words = []
    
    def prefix(self, s: str) -> TreeNode:
        if s not in self.children:
            return None
        return self.children[s]

class Trie:
    def __init__(self):
        self.root = TreeNode()

    def add(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.words.append(word)
            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)
        
        res = set()
        def search(i: int, j:int, node: TreeNode, visited: set):
            if i < 0 or j < 0:
                return 
            if i >= ROWS or j >= COLS:
                return 
            if (i,j) in visited:
                return
            node = node.prefix(board[i][j])
            if not node:
                return
            for w in node.words:
                res.add(w)
            visited.add((i,j))
            search(i+1, j, node, visited)
            search(i-1, j, node, visited)
            search(i, j+1, node, visited)
            search(i, j-1, node, visited)
            visited.remove((i,j))
            
        ROWS, COLS = len(board), len(board[0])
        for i in range(ROWS):
            for j in range (COLS):
                search(i, j, trie.root, set())
        return list(res)