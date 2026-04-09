
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        group = []
        cur_cap = 0
        for num, pickup, dropoff in trips:
            while group and group[0].dropoff <= pickup:    
                dropped_group = heapq.heappop(group)
                cur_cap -= dropped_group.num
            
            cur_cap += num
            heapq.heappush(group, Group(num, dropoff))
            
            if cur_cap > capacity:
                return False
        return True

class Group:
    def __init__(self, num, dropoff):
        self.num = num
        self.dropoff = dropoff
    
    def __lt__(self, other):
        return self.dropoff < other.dropoff