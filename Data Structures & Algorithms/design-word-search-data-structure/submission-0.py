class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        return self.pattern_search(self.root, 0, word)

    def pattern_search(self, next: Node, i: int, word: str) -> bool:
        if i == len(word):
            return next.word
        if word[i] == '.':
            for val in next.children.values():
                if self.pattern_search(val, i+1, word):
                    return True
            return False
        if word[i] not in next.children:
            return False
        return self.pattern_search(next.children[word[i]], i+1, word)