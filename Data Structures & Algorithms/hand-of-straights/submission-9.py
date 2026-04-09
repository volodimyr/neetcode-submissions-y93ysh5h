class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        if N % groupSize:
            return False
        counter = Counter(hand)
        for n in hand:
            if not counter[n]:
                continue
            start = n
            while counter[start-1]:
                start -= 1
            
            c = 0
            while c < groupSize:
                if not counter[start]:
                    return False
                c += 1
                counter[start] -= 1
                start += 1

        for _, v in counter.items():
            if v > 0:
                return False
        
        return True