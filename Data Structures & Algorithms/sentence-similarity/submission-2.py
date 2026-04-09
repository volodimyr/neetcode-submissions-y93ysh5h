class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        N, M = len(sentence1), len(sentence2)
        if N != M:
            return False
        
        present = set()
        for p1, p2 in similarPairs:
            present.add((p1,p2))
        
        for i in range(len(sentence1)):
            p1, p2 = sentence1[i], sentence2[i]
            if p1 == p2:
                continue
            if (p1,p2) in present or (p2,p1) in present:
                continue
            return False

        return True
