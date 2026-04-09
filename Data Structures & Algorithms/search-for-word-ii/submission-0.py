class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class SearchResult:
    def __init__(self, has_prefix: bool, words: List[str]):
        self.has_prefix = has_prefix
        self.words = words

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.words.append(word)
    
    def prefix(self, board: List[List[str]], seq: List[Tuple]) -> SearchResult:
        cur = self.root
        for i, j in seq:
            if board[i][j] not in cur.children:
                return SearchResult(False, [])
            cur = cur.children[board[i][j]]
        return SearchResult(True, cur.words)
            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)
        
        res = set()
        def search(i: int, j: int, seq: List[str]):
            if i < 0 or j < 0:
                return 
            if i >= ROWS or j >= COLS:
                return 
            if (i,j) in seq:
                return
            seq.append((i,j))
            result = trie.prefix(board, seq)
            if result.has_prefix:
                for w in result.words:
                    res.add(w)
                search(i+1, j, seq)
                search(i-1, j, seq)
                search(i, j+1, seq)
                search(i, j-1, seq)
            seq.remove((i,j))
            
        ROWS, COLS = len(board), len(board[0])
        for i in range(ROWS):
            for j in range (COLS):
                search(i, j, [])
        
        return list(res)