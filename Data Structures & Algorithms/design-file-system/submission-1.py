class FileSystem:

    def __init__(self):
        self.trie = Trie()

    def createPath(self, path: str, value: int) -> bool:
        return self.trie.insert(path, value) if self.trie.validate(path) else False

    def get(self, path: str) -> int:
        return self.trie.get(path) if self.trie.validate(path) else -1


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def validate(self, path: str):
        steps = path.split('/')
        for step in steps[1:]:
            if step == '' or step == '/':
                return False
        return True

    def insert(self, path: str, value: int):
        cur = self.root
        steps = path.split('/')[1:]
        N = len(steps)

        for i in range(N-1):
            step = steps[i]
            if step not in cur.ch:
                return False
            cur = cur.ch[step]

        last = steps[N-1]
        if last in cur.ch:
            return False
        else:
            cur.ch[last] = TrieNode()
            cur = cur.ch[last]
        
        cur.val = value
        return True
    
    def get(self, path: str):
        cur = self.root
        for step in path.split("/")[1:]:
            if step not in cur.ch:
                return -1
            cur = cur.ch[step]
        return cur.val

class TrieNode:
    def __init__(self):
        self.ch = {}
        self.val = -1

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
