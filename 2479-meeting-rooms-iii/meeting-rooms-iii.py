class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        '''
        - to get the room with the lowest room => available_rooms = min heap (room_idx)
        - to store waiting meetings => queue in arrival order of meeting start time 
        - to store busy rooms => min heap (free_at, room_idx)
        '''
        meetings.sort() 

        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        busy_rooms = []

        count = [0] * n

        for (start, end) in meetings:
            duration = end - start
            # free all busy rooms 
            while busy_rooms and busy_rooms[0][0] <= start: 
                _, room_idx = heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms, room_idx)
            
            if available_rooms: 
                room_idx = heapq.heappop(available_rooms)
                count[room_idx] += 1
                heapq.heappush(busy_rooms, (end, room_idx))
            else:
                free_at, room_idx = heapq.heappop(busy_rooms)
                count[room_idx] += 1
                heapq.heappush(busy_rooms, (free_at + duration, room_idx))
            
        return count.index(max(count))

