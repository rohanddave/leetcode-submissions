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

        waiting_meetings = collections.deque()
        i = 0

        busy_rooms = [] # min heap (free_at, room_idx)
        
        curr_time = meetings[0][0]

        count = [0] * n

        while i < len(meetings) or waiting_meetings: 
            # add all meetings that started
            while i < len(meetings) and meetings[i][0] <= curr_time: 
                waiting_meetings.append(meetings[i])
                i += 1
            
            # free all busy rooms 
            while busy_rooms and busy_rooms[0][0] <= curr_time:
                _, room_idx = heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms, room_idx)
            
            # schedule max work
            while waiting_meetings and available_rooms: 
                meeting = waiting_meetings.popleft() 
                room_idx = heapq.heappop(available_rooms)
                count[room_idx] += 1
                meeting_duration = meeting[1] - meeting[0] # check off by one error
                free_at = curr_time + meeting_duration
                heapq.heappush(busy_rooms, (free_at, room_idx))
            
            if waiting_meetings and busy_rooms: 
                curr_time =  busy_rooms[0][0]
            elif not waiting_meetings and i < len(meetings):
                curr_time = meetings[i][0]
        return count.index(max(count))

        