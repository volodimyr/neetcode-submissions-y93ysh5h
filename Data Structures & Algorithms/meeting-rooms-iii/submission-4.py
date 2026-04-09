class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = [i for i in range(n)]
        heapq.heapify(rooms)
        booked = []   
        count = [0] * n

        for start, end in meetings:
            while booked and start >= booked[0][0]:
                _, room = heapq.heappop(booked)
                heapq.heappush(rooms, room)
            
            if rooms:
                room = heapq.heappop(rooms)
                heapq.heappush(booked, (end, room))
            else:
                endp, room = heapq.heappop(booked)
                end = (end-start) + endp
                heapq.heappush(booked, (end, room))

            count[room] += 1



        return count.index(max(count))