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

            # if start == n:
            #     continue
            
            c = 0
            while c < groupSize:
                if not counter[start]:
                    return False
                c += 1
                counter[start] -= 1
                start += 1

        
        return True