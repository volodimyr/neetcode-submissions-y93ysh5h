class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        if N % groupSize:
            return False
        hand.sort()
        counter = Counter(hand)
        for n in hand:
            if not counter:
                break
            if n not in counter:
                continue
            c = 0
            while counter[n] > 0 and c < groupSize:
                counter[n] -= 1
                if counter[n] <= 0:
                    del counter[n]
                c+=1
                n+=1

            if c != groupSize:
                return False

        return len(counter) == 0