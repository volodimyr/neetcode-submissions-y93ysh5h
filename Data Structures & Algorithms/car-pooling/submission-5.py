class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        min_heap_trips = []
        for t in trips:
            heapq.heappush(min_heap_trips, Trips(t[0], t[1], t[2]))

        min_heap_car_group = []
        
        cur_time = 0
        cur_cap = 0
        while min_heap_trips:
            trip = heapq.heappop(min_heap_trips)
            cur_time = trip.pickup
            cur_cap += trip.num
            while min_heap_car_group:    
                if min_heap_car_group[0].dropoff <= cur_time:
                    group = heapq.heappop(min_heap_car_group)
                    cur_cap -= group.num
                else:
                    break
            
            heapq.heappush(min_heap_car_group, CarGroup(trip.num, trip.dropoff))
            if capacity < cur_cap:
                return False

        return True

class CarGroup:
    def __init__(self, num, dropoff):
        self.num = num
        self.dropoff = dropoff
    
    def __lt__(self, other):
        return self.dropoff < other.dropoff

class Trips:
    def __init__(self, num, pickup, dropoff):
        self.num = num
        self.pickup = pickup
        self.dropoff = dropoff
    
    def __lt__(self, other):
        return self.pickup < other.pickup