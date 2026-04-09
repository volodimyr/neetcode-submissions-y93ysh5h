class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        min_heap = []
        for t in trips:
            heapq.heappush(min_heap, Group(t[0], t[1], t[2]))

        heading = []
        while min_heap:
            group = heapq.heappop(min_heap)
            for h in heading[:]:
                if group.pickup >= h[1]:
                    heading.remove(h)
            heading.append([group.num, group.dropoff])
            if cur_cap(heading) > capacity:
                return False
        return True

def cur_cap(cur: List[List[int]]) -> int:
    sum = 0
    for c in cur:
        sum += c[0]
    return sum

class Group:
    def __init__(self, num, pickup, dropoff):
        self.num = num
        self.pickup = pickup
        self.dropoff = dropoff
    
    def __lt__(self, other):
        return self.pickup < other.pickup