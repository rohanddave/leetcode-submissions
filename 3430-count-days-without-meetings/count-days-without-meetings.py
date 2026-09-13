class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        def does_overlap(a, b): 
            return not (a[0] > b[1] or a[1] < b[0])
        
        meetings.sort()
        latest = meetings[0]
        available = [1, days]
        res = days

        for i in range(1, len(meetings)): 
            if does_overlap(latest, meetings[i]):
                latest[1] = max(meetings[i][1], latest[1])
            else: 
                interval = latest
                intersection = [max(available[0], interval[0]), min(available[1], interval[1])]
                overlap = intersection[1] - intersection[0] + 1
                if overlap > 0:
                    res -= overlap
                latest = meetings[i]
        interval = latest
        intersection = [max(available[0], interval[0]), min(available[1], interval[1])]
        overlap = intersection[1] - intersection[0] + 1
        if overlap > 0:
            res -= overlap
        return res

