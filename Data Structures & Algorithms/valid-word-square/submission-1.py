class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        for r in range(len(words)):
            for c in range(len(words[r])):
                try:
                    if words[r][c] != words[c][r]:
                        return False
                except IndexError:
                    return False
        
        return True