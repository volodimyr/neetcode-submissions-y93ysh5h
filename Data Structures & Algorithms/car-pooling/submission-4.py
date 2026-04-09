class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        min_heap = []
        for t in trips:
            heapq.heappush(min_heap, Group(t[0], t[1], t[2]))

        car = Car(capacity, 0)
        while min_heap:
            group = heapq.heappop(min_heap)
            car.drop(group.pickup)
            car.add(group.num, group.dropoff)
            if car.reached_max():
                return False
        return True

class Car:
    def __init__(self, capacity, cur_capacity):
        self.capacity = capacity
        self.cur_capacity = cur_capacity
        self.group = []
    
    def add(self, num, dropoff):
        self.cur_capacity += num
        self.group.append([num, dropoff])
    
    def drop(self, cur_time):
        for g in self.group[:]:
            if cur_time >= g[1]:
                self.group.remove(g)
                self.cur_capacity -= g[0]
    
    def reached_max(self):
        return self.capacity < self.cur_capacity

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