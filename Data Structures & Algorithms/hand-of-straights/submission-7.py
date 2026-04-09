class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        if N % groupSize:
            return False
        counter = Counter(hand)
        for n in hand:
            if n not in counter:
                continue
            start = n
            while counter[start-1]:
                start -= 1
            
            for _ in range(groupSize):
                if start not in counter:
                    return False
                if counter[start] == 1:
                    del counter[start]
                else:
                    counter[start] -= 1
                start+=1

        
        return len(counter) == 0