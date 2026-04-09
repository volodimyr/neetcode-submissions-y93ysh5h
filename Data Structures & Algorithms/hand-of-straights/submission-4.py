class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        counter = Counter(hand)

        def helper(start, clean=False):
            c = 0
            while start in counter:
                if clean:
                    if counter[start] == 1:
                        del counter[start]
                    else:
                        counter[start] -= 1
                start += 1
                c += 1
                if c == groupSize:
                    return True
            return False

        while counter:
            start = -1
            for k in counter:
                if helper(k):
                    start = k
            if start == -1:
                break
            else:
                helper(start, True)
        
        return len(counter) == 0