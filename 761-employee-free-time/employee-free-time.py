"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        n = len(schedule) 
        heap = [] 

        for i in range(n): 
            start, end = schedule[i][0].start, schedule[i][0].end
            heapq.heappush(heap, (start, end, i, 0))
        
        def does_overlap(a, b): 
            return not (a[0] > b[1] or a[1] < b[0])
        
        merged = []
        while heap:
            start, end, person_idx, idx = heapq.heappop(heap)

            # insert into merged array
            if merged and does_overlap(merged[-1], [start, end]):
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

            if idx + 1 < len(schedule[person_idx]):
                start, end = schedule[person_idx][idx + 1].start, schedule[person_idx][idx + 1].end
                heapq.heappush(heap, (start, end, person_idx, idx + 1))
        
        res = []
        for i in range(len(merged) - 1):
            res.append(Interval(merged[i][1],merged[i + 1][0]))
        return res

        