class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a:
            heapq.heappush(max_heap, Letter('a', a))
        if b:
            heapq.heappush(max_heap, Letter('b', b))
        if c:
            heapq.heappush(max_heap, Letter('c', c))
        
        s = ''
        while max_heap:
            next = heapq.heappop(max_heap)
            if len(s) > 1 and s[-1] == next.letter and s[-2] == next.letter:
                if not max_heap:
                    break
                delim = heapq.heappop(max_heap)
                s += delim.letter
                delim.times-=1
                if delim.times:
                    heapq.heappush(max_heap, delim)
                heapq.heappush(max_heap, next)
                continue
            s += next.letter
            next.times-=1
            if next.times:
                heapq.heappush(max_heap, next)
    
        return s

class Letter:
    def __init__(self, letter, times):
        self.letter = letter
        self.times = times

    def __lt__(self, other):
        return self.times > other.times