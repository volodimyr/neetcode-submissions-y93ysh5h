class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = []
        for i in range(n):
            heapq.heappush(rooms, (i,None))
        
        booked = []   
        m = defaultdict(int)

        j = 0
        while j < len(meetings):
            start, finish = meetings[j]
            poped = False
            while booked and start >= booked[0][0]:
                poped = True
                finish_pop, room = heapq.heappop(booked)
                heapq.heappush(rooms, (room, finish_pop))

            if rooms:
                room, finish_pop = heapq.heappop(rooms)
                if finish_pop and finish_pop > start:
                    finish = (finish-start) + finish_pop

                heapq.heappush(booked, (finish, room))
                m[room] += 1
                j += 1
            elif not poped:
                finish_pop, room = heapq.heappop(booked)
                heapq.heappush(rooms, (room, finish_pop))


        most = [-1, -1]
        for room, booked in m.items():
            if booked > most[1]:
                most[0] = room
                most[1] = booked
            elif booked == most[1]:
                if room < most[0]:
                    most[0] = room
                    most[1] = booked


        return most[0]