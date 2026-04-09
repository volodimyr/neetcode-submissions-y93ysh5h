class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        for r in range(len(words)):
            for c in range(len(words[r])):
                if c >= len(words):
                    return False
                if r >= len(words[c]):
                    return False
                if words[r][c] != words[c][r]:
                    return False
        return True