class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = [] 
        for (start, end) in intervals:
            events.append((start, 1))
            events.append((end, -1))
        events.sort() 

        res = 0
        curr_sum = 0
        for _, delta in events: 
            curr_sum += delta
            res = max(res, curr_sum)
        
        return res
            

        