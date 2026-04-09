class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        min_heap_car_group = []
        cur_cap = 0
        for num, pickup, dropoff in trips:
            cur_cap += num
            while min_heap_car_group and min_heap_car_group[0].dropoff <= pickup:    
                group = heapq.heappop(min_heap_car_group)
                cur_cap -= group.num
            heapq.heappush(min_heap_car_group, CarGroup(num, dropoff))
            if capacity < cur_cap:
                return False

        return True

class CarGroup:
    def __init__(self, num, dropoff):
        self.num = num
        self.dropoff = dropoff
    
    def __lt__(self, other):
        return self.dropoff < other.dropoff