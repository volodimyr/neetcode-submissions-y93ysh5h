class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        set_words = set(wordList)
        if endWord not in set_words:
            return 0
        q = deque()
        q.append((beginWord, 1))
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        while q:
            pop, steps = q.popleft()
            if pop == endWord:
                return steps

            for i in range(len(pop)):
                for char in chars:
                    if char == pop[i]:
                        continue
                    mutation = pop[:i] + char + pop[i+1:]
                    if mutation in set_words:
                        set_words.discard(mutation)
                        q.append((mutation, steps+1))
        return 0