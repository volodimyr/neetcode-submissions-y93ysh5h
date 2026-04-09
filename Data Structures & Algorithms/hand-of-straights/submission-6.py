class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        if N % groupSize:
            return False
        counter = Counter(hand)
        for n in hand:
            if n not in counter:
                continue
            if not counter:
                return True
            
            if counter[n] == 1:
                del counter[n]
            else:
                counter[n] -= 1

            c = 1
            if c == groupSize:
                continue

            org = n
            n -= 1
            while n in counter:
                c += 1
                if counter[n] == 1:
                    del counter[n]
                else:
                    counter[n] -= 1
                n -= 1
                if c == groupSize:
                    break
            
            if c == groupSize:
                continue
            
            n = org+1
            while n in counter:
                c += 1
                if counter[n] == 1:
                    del counter[n]
                else:
                    counter[n] -= 1
                n += 1
                if c == groupSize:
                    break
            
            if c != groupSize:
                return False

        
        return True